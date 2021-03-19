school=1
school_principle=50000
school_peon=10000
school_teachers=25000

school_tax=30000

school_teachers=30000

total_school=(school*school_principle)+(school*school_peon)+(school*school_teachers)

total_salarytax=(total_school-school_tax)

print("total salarytax=",total_salarytax)
print("total salary=",total_school)