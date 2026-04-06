import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import plotly.io as pio


pio.templates.default = "simple_white"


def oneline(sheet_name,reflist):
    data = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name, index_col="Date", parse_dates=True)
    fig = px.line(data, x=data.index, y=reflist[0], title=reflist[1])
    fig.write_html("my-project/docs/charts/" + sheet_name + ".html", include_plotlyjs='cdn')


def onebar(sheet_name,reflist):
    data = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name, index_col="Date", parse_dates=True)
    fig = px.bar(data,x=data.index,y=reflist[0],
    title=reflist[1],
    color=data[reflist[0]]<0,
    color_discrete_map = {True:'red', False:'blue'})

    fig.update_layout(showlegend=False)

    fig.write_html("my-project/docs/charts/" + sheet_name + ".html", include_plotlyjs='cdn')

def twoline(sheet_name1,sheet_name2,reflist,same_axis=True):
    data1 = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name1, index_col="Date", parse_dates=True)
    data2 = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name2, index_col="Date", parse_dates=True)
    

    if same_axis == True:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x = data1.index,
            y = data1[reflist[0][0]],
            name=reflist[0][1]
        ))

        fig.add_trace(go.Scatter(
            x = data2.index,
            y = data2[reflist[1][0]],
            name=reflist[1][1]
        ))


    
    if same_axis == False:
        fig = make_subplots(specs=[[{"secondary_y":True}]])

        fig.add_trace(
            go.Scatter(
            x = data1.index,
            y = data1[reflist[0][0]],
            name=reflist[0][1]
            ), secondary_y=False
        )

        fig.add_trace(go.Scatter(
            x = data2.index,
            y = data2[reflist[1][0]],
            name=reflist[1][1]
        ), secondary_y=True
        )


    common_start = max(data1.index.min(), data2.index.min())
    common_end = max(data1.index.max(), data2.index.max())

    fig.update_xaxes(range=[common_start,common_end])

    fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",  # 왼쪽 기준
                x=0              # 가장 왼쪽
            ),
            title=reflist[0][1]+" & "+reflist[1][1]
        )

    fig.write_html("my-project/docs/charts/" + sheet_name1 + ".html", include_plotlyjs='cdn')

def twobar(sheet_name1,sheet_name2,reflist):
    data1 = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name1, index_col="Date", parse_dates=True)
    data2 = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name2, index_col="Date", parse_dates=True)

    fig = go.Figure(data=[
        go.Bar(name='By_Iran',x=data1.index,y=data1['BY_IRAN']),
        go.Bar(name='AGAINST_Iran',x=data2.index,y=data2['AGAINST_IRAN']),
    ])

    fig.update_layout(barmode='group', title=reflist[0][1]+" & "+reflist[1][1])
    fig.write_html("my-project/docs/charts/" + sheet_name1 + ".html", include_plotlyjs='cdn')

    # fig = go.Figure(data[
    #     go.Bar(name="BY_IRAN",x=data1.index),
    #     # go.Bar(name="AGAINST_IRAN",x=data2.index, y=data2.values),
    # ])
    # fig.update_layout(barmode='group')
    # fig.show()


def table_bar(sheet_name, title):
    data = pd.read_excel("my-project/data.xlsx", sheet_name=sheet_name)
    data.index = data[data.columns[0]]
    data.drop(data.columns[0], axis=1, inplace=True)

    fig = px.bar(data,x=data.index,y=data.columns)
    fig.update_layout(title=title)
    fig.write_html("my-project/docs/charts/" + sheet_name + ".html", include_plotlyjs='cdn')



if __name__ == "__main__":
    oneline_dic = {}
    oneline_dic["usurtot"] = ["usurtot index","Unemployment Rate"]
    oneline_dic["concjobp"] = ["concjobp index","Consumer Confidence Job Plentyful"]
    oneline_dic['vix'] = ["vix index","Vix index"]
    oneline_dic['goldsilver'] = ["goldsilver index","Gold/Silver Ratio"]
    oneline_dic['napmempl'] = ["napmempl index","ISM Manf. Employment"]
    oneline_dic['napmpmi'] = ["napmpmi index","ISM Manf. Index"]
    oneline_dic['napmpric'] = ["napmpric index","ISM Manf. Prices"]
    oneline_dic['napmnemp'] = ["napmnemp index","ISM Service Employment"]
    oneline_dic['napmnmi'] = ["napmnmi index","ISM Service Index"]
    oneline_dic['indduois'] = ["indduois index","Indeed Overall Job posting"]
    oneline_dic['napmnprc'] = ["napmnprc index","ISM Service Prices"]
    oneline_dic['joltopen'] = ["joltopen index","US Job opening Rate%"]
    oneline_dic['chaltotl'] = ["chaltotl index","Challenger US Job cut announcements"]
    oneline_dic['sboitotl'] = ['sboitotl index',"NFIB Small Business optimism"]
    
    oneline_dic['mpmicama'] = ["mpmicama index","Canada Manf. PMI"]
    oneline_dic['iveysa'] = ["iveysa index","Ivey PMI"]
    oneline_dic['canlxemr'] = ["canlxemr index","Unemployment Rate"]
    oneline_dic['camfchng'] = ["camfchng index","Manufacturing Sales MoM"]
    oneline_dic['caheperm'] = ["caheperm index","Average Hourly wage rate of permanent workers YoY%"]
    oneline_dic['econcrea'] = ["econcrea index","Canada Existing Home Sales MoM%"]
    oneline_dic['3agsreg'] = ["3agsreg index","US Average Gasoline Price"]
    oneline_dic['ttfg1mon'] = ["ttfg1mon index","Netherlands TTF Natural Gas Forward 1 (EUR/MWh)"]
    oneline_dic['cl1'] = ["cl1 comdty","WTI ($ per barrel)"]
    oneline_dic['co1cl1'] = ["co1-cl1","Brent - WTI spread ($ per barrel)"]
    oneline_dic['gcfpnpki'] = ["gcfpnpki index","North America Fertilizer Price index"]
    oneline_dic['fzwwwst'] = ["fzwwwst index","Global Crude oil on water (thou barrels)"]
    oneline_dic['outfgaf'] = ["outfgaf index","Philadelphia Fed Business Outlook"]
    oneline_dic['spx_pe'] = ["spx index","S&P500 index PER (12M Fwd Blend)"]
    oneline_dic['chpmindx'] = ["chpmindx index","Chicago Business Barometer SA"]
    oneline_dic['concconf'] = ["concconf index","Conference Board Consumer Confidence"]

    onebar_dic = {}
    onebar_dic['canlnetj'] = ['canlnetj index',"Canada Employment Change"]
    onebar_dic['nfp tch'] = ['nfp tch index',"Non Farm Payrolls MoM chgs"]
    onebar_dic['adp chng'] = ["adp chng index","ADP private Nonfarm change"]
    onebar_dic['csxhspcm'] = ["csxhspcm index","CPI Super Core MoM%"]
    onebar_dic['trhwcoct'] = ["trhwcoct index","Hormuz Strait Number of Oil Tankers and Transit Volume (West to East, 7d Total)"]
    onebar_dic['trhwtkct'] = ["trhwtkct index","Hormuz Strait Number of Tankers and Transit Volume (West to East, 7d Total)"]
    onebar_dic['trhecoct'] = ["trhecoct index","Hormuz Strait Number of Oil Tankers and Transit Volume (East to West, 7d Total)"]
    onebar_dic['trhetkct'] = ["trhetkct index","Hormuz Strait Number of Tankers and Transit Volume (East to West, 7d Total)"]
    onebar_dic['hpimmom%'] = ["hpimmom% index","US House Price index purchase only MoM%"]
    onebar_dic['cagdpmom'] = ["cagdpmom index","Canada GDP MoM"]


    twoline_dic = {}
    twoline_dic['conspxme consp5me'] = [["conspxme index","Consumer Confi. 1Y inflatiion exp",True],["consp5me index","Consumer Confi. 5Y inflatiion exp",True]]
    twoline_dic['trufusyy cpi_xyoy'] = [['trufusyy index',"Truflation YoY",True],['cpi xyoy index',"CPI Core YoY",False]]
    twoline_dic['injcjc injcjc'] = [['injcjc index',"Initial Jobless",True],['injcsp index',"Continuing Claims",False]]
    twoline_dic['jltsquis jltsquis'] = [['jltsquis index',"JOLTS Job quits level",True],['jltslays index',"JOLTS Layoffs",False]]
    twoline_dic['conspxmd conspxmd'] = [['conspxmd index',"Umich 1Y inflation exp",True],['consp5md index',"Umich 5-10Y inflation exp",True]]
    twoline_dic['usjllvr% usjllvr%'] = [['usjllvr% index',"Job leavers Rate",True],['userlayo index',"Permanent Job losers rate",False]]
    twoline_dic['bm7t sox'] = [['bm7t index',"Mag7 Index",True],['sox index',"Sox Index",False]]
    twoline_dic['cpi_yoy cpi_yoy'] = [['cpi xyoy index',"CPI Core YoY%",True],['cpi yoy index',"CPI YoY%",True]]
    twoline_dic['usswit1 usggbe05'] = [['usswit1 curncy',"US Inflation Swap 1 Year",True],['usggbe05 index',"US 5Y breakeven",True]]
    twoline_dic['rcpptdis rcpptdis'] = [['rcpptdis index',"Trump disapproval rating",True],['rcpptapp index',"Trump approval rating",True]]
    twoline_dic['plymc295 plymc295'] = [['plymc295 index',"Prob. Dem. control senate after midterm",True],['plymc29e index',"Prob. Dem. control house after midterm",True]]
    twoline_dic['dfedgba dfedgba'] = [['dfedgba index',"Dallas Fed Manufacturing Outlook",True],['dsergbcc index',"Dallas Fed Service Outlook",True]]
    twoline_dic['spcs20y% spcs20y%'] = [['spcs20y% index',"Case-shiller 20city home price index YoY%",True],['spcsusay index',"US national home price YoY%",True]]

    twobar_dic ={}
    twobar_dic['h.iranconflict h.iranconflict'] = [['h.iranconflict',"Strike by Iran"],['h.iranconflict',"Strike into Iran"]]


    tablebar_dic = {}
    tablebar_dic['returns_regions'] = ['returns_region',"Returns by Region"]
    tablebar_dic['returns_assetclass'] = ['returns_assetclass',"Returns by Asset Class"]

    
    for sheet_name, reflist in oneline_dic.items():
        oneline(sheet_name, reflist)
    
    for sheet_name, reflist in onebar_dic.items():
        onebar(sheet_name, reflist)

    for sheet_name, reflist in twoline_dic.items():
        sheet_name1 = sheet_name.split()[0]
        sheet_name2 = sheet_name.split()[1]

        twoline(sheet_name1,sheet_name2,reflist,same_axis=reflist[1][2])
    
    for sheet_name, reflist in tablebar_dic.items():
        table_bar(sheet_name, reflist[1])
    
    for sheet_name,reflist in twobar_dic.items():
        sheetname1 = sheet_name.split()[0]
        sheetname2 = sheet_name.split()[1]

        twobar(sheetname1,sheetname2,reflist)




