# python-program--get-season
This program identifies the season based on user-provided date and month inputs
1, define seasons:
  winter from dec.16th to mar.15th
  spring from mar.16th to jun.15th
  summer from jun.16th to sep.15th
  fall   from sep.16th to dec.15th
2, create functions to make the code can be used frequently
3,questions:
---(1)handle month that span across 2 years
def get_season(m, d):
    md = m * 100 + d

    if md >= 1216 or md <= 315:
        return "Winter"
    elif 316 <= md <= 615:
        return "Spring"
    elif 616 <= md <= 915:
        return "Summer"
    else:
        return "Fall"
