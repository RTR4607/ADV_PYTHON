import pygal
b_chart=pygal.Pie()
b_chart.title="protocol Details"
b_chart.add("TCp",15)
b_chart.add("UDP",30)
b_chart.add("ICMP",45)
b_chart.add("OTHERS",10)
b_chart.render_to_file('pie_charrt.png')
b_chart.render_in_browser()

