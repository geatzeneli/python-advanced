informacionet={
    "Geat": 6000,
    "Filani": 1400,
    "Fisteku": 2400
}
print(informacionet)

rroga = (informacionet["Geat"])
print(rroga)


#print(informacionet.keys())
#print(informacionet.values())

informacionet["Geat"]=10000
informacionet["Filani"]=2300
print(informacionet)
print(informacionet.keys())
print(informacionet.values())

del informacionet["Fisteku"]
print(informacionet)