#
# first injest the input list
#

hostsFile = open("./input.txt", "r")

# using set to avoid duplicates
domains = set()

for line in hostsFile:
    # remove leading/trailing white space
    line = line.strip()
    
    # allow comments
    if line.startswith("#"):
        continue
    
    # skip blank lines
    if len(line) == 0:
        continue
    
    # NOTE - this escapes all .'s but does NOT check for them being part of a regex etc
    domains.add(line.replace(".", "\\\\."))


hostsFile.close()


#
# write out the JSON
#

count = 0
output = open("output.txt", "w")

# open the rules array
output.writelines("[\r")

# change to list mostly to make it easy to check for the last item
domains = list(domains)

# loop through the list of domains
for domain in domains:
    count += 1
    
    s = "{ \"id\":"+str(count)+",\"priority\":1,\"action\":{\"type\":\"block\"},\"condition\":{\"regexFilter\":\"http(s)?://(.*\\\\.)?"+domain+".*\",}}"
    
    # leave off the last comma
    if domain != domains[-1]:
        s += ","

    s += "\r"
    
    output.writelines(s)


# close the rules array
output.writelines("]")

output.close()

print(f"produced {count} domains")
