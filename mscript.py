# 设置背景为白色同时隐藏化合价
cmd.set("valence", 0)
cmd.bg_color("white")
# 清理视图
cmd.hide ("everything")
cmd.show ("cartoon","polymer")
cmd.show("sticks","organic")
# 选择配体
cmd.select ("ligand","resn Q8V")
# 选择配体3.2埃范围内的小分子残基,并呈现为棒状结构
cmd.select("active", "byres polymer within 3.2 of ligand")
cmd.select("active_site", "ligand or byres polymer within 3.2 of ligand")
cmd.show("sticks","active")
# 美化
cmd.set("cartoon_transparency", 0.4, "polymer")
cmd.color("white","polymer and active" )
# 展示氢键
cmd.distance("hbonds", "active_site and polymer", "active_site and not polymer", 3.2, mode=2)
cmd.show("dashes", "hbonds")
# 修复蛋白质为白色同时active_site按照元素染色
util.cbag("ligand")    
cmd.color("white", "polymer")
util.cbag("active and not elem C") 
cmd.hide("labels", "all")