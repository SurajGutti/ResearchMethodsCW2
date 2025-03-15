import pandas

diet_groups_m = {}
diet_groups_f = {}

env_impact_f = {}
env_impact_m = {}

results = pandas.read_csv('Results_21Mar2022.csv')

for index, row in results.iterrows():
    if row.sex == "male":
        if row.diet_group in diet_groups_m:
            diet_groups_m[row.diet_group] += 1
        else:
            diet_groups_m[row.diet_group] = 1

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
    elif row.sex == "female":
        if row.diet_group in diet_groups_f:
            diet_groups_f[row.diet_group] += 1
        else:
            diet_groups_f[row.diet_group] = 1

print(diet_groups_m)
print(diet_groups_f)

# df = pandas.DataFrame(env_impact)
# df.insert(0, "Impact Type", ['GreenHouseGas', 'CH4', 'N2O', 'LandUsed', 'WaterScarcity', 'Eutrophication', 'WaterUse', 'Acid'])
#
# df.to_excel('diet_groups.xlsx', sheet_name='sheet1', index=False)
