import pandas

age_groups = {}

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
    if row.age_group in age_groups:
        age_groups[row.age_group] += 1
    else:
        age_groups[row.age_group] = 1

    if row.age_group in mean_ghg:
        mean_ghg[row.age_group] += row.mean_ghgs
    else:
        mean_ghg[row.age_group] = row.mean_ghgs

    if row.age_group in mean_ch4:
        mean_ch4[row.age_group] += row.mean_ghgs_ch4
    else:
        mean_ch4[row.age_group] = row.mean_ghgs_ch4

    if row.age_group in mean_n2o:
        mean_n2o[row.age_group] += row.mean_ghgs_n2o
    else:
        mean_n2o[row.age_group] = row.mean_ghgs_n2o

    if row.age_group in mean_land:
        mean_land[row.age_group] += row.mean_land
    else:
        mean_land[row.age_group] = row.mean_land

    if row.age_group in mean_watscar:
        mean_watscar[row.age_group] += row.mean_watscar
    else:
        mean_watscar[row.age_group] = row.mean_watscar

    if row.age_group in mean_eut:
        mean_eut[row.age_group] += row.mean_eut
    else:
        mean_eut[row.age_group] = row.mean_eut

    if row.age_group in mean_watuse:
        mean_watuse[row.age_group] += row.mean_watuse
    else:
        mean_watuse[row.age_group] = row.mean_watuse

    if row.age_group in mean_acid:
        mean_acid[row.age_group] += row.mean_acid
    else:
        mean_acid[row.age_group] = row.mean_acid

for group, value in age_groups.items():
    average_ghg[group] = mean_ghg[group] / age_groups[group]
    average_ch4[group] = mean_ch4[group] / age_groups[group]
    average_n2o[group] = mean_n2o[group] / age_groups[group]
    average_land[group] = mean_land[group] / age_groups[group]
    average_watscar[group] = mean_watscar[group] / age_groups[group]
    average_eut[group] = mean_eut[group] / age_groups[group]
    average_watuse[group] = mean_watuse[group] / age_groups[group]
    average_acid[group] = mean_acid[group] / age_groups[group]

env_impact = average_ghg, average_ch4, average_n2o, average_land, average_watscar, average_eut, average_watuse, average_acid

df = pandas.DataFrame(env_impact)
df.insert(0, "Impact Type", ['GreenHouseGas', 'CH4', 'N2O', 'LandUsed', 'WaterScarcity', 'Eutrophication', 'WaterUse', 'Acid'])

df.to_excel('age_groups.xlsx', sheet_name='sheet1', index=False)
