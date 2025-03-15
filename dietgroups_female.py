import pandas

diet_groups = {}

mean_ghg = {}
average_ghg = {}

mean_ch4 = {}
average_ch4 = {}

mean_n2o = {}
average_n2o = {}

mean_land = {}
average_land = {}

mean_watscar = {}
average_watscar = {}

mean_eut = {}
average_eut = {}

mean_watuse = {}
average_watuse = {}

mean_acid = {}
average_acid = {}

results = pandas.read_csv('Results_21Mar2022.csv')

for index, row in results.iterrows():
    if row.sex == "female":
        if row.diet_group in diet_groups:
            diet_groups[row.diet_group] += 1
        else:
            diet_groups[row.diet_group] = 1

        if row.diet_group in mean_ghg:
            mean_ghg[row.diet_group] += row.mean_ghgs
        else:
            mean_ghg[row.diet_group] = row.mean_ghgs

        if row.diet_group in mean_ch4:
            mean_ch4[row.diet_group] += row.mean_ghgs_ch4
        else:
            mean_ch4[row.diet_group] = row.mean_ghgs_ch4

        if row.diet_group in mean_n2o:
            mean_n2o[row.diet_group] += row.mean_ghgs_n2o
        else:
            mean_n2o[row.diet_group] = row.mean_ghgs_n2o

        if row.diet_group in mean_land:
            mean_land[row.diet_group] += row.mean_land
        else:
            mean_land[row.diet_group] = row.mean_land

        if row.diet_group in mean_watscar:
            mean_watscar[row.diet_group] += row.mean_watscar
        else:
            mean_watscar[row.diet_group] = row.mean_watscar

        if row.diet_group in mean_eut:
            mean_eut[row.diet_group] += row.mean_eut
        else:
            mean_eut[row.diet_group] = row.mean_eut

        if row.diet_group in mean_watuse:
            mean_watuse[row.diet_group] += row.mean_watuse
        else:
            mean_watuse[row.diet_group] = row.mean_watuse

        if row.diet_group in mean_acid:
            mean_acid[row.diet_group] += row.mean_acid
        else:
            mean_acid[row.diet_group] = row.mean_acid

for group, value in diet_groups.items():
    average_ghg[group] = mean_ghg[group] / diet_groups[group]
    average_ch4[group] = mean_ch4[group] / diet_groups[group]
    average_n2o[group] = mean_n2o[group] / diet_groups[group]
    average_land[group] = mean_land[group] / diet_groups[group]
    average_watscar[group] = mean_watscar[group] / diet_groups[group]
    average_eut[group] = mean_eut[group] / diet_groups[group]
    average_watuse[group] = mean_watuse[group] / diet_groups[group]
    average_acid[group] = mean_acid[group] / diet_groups[group]

env_impact = average_ghg, average_ch4, average_n2o, average_land, average_watscar, average_eut, average_watuse, average_acid

df = pandas.DataFrame(env_impact)
df.insert(0, "Impact Type", ['GreenHouseGas', 'CH4', 'N2O', 'LandUsed', 'WaterScarcity', 'Eutrophication', 'WaterUse', 'Acid'])

df.to_excel('diet_groups_female.xlsx', sheet_name='female', index=False)
