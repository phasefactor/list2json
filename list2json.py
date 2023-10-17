hostsFile = open("./input.txt", "r")

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
    
    domains.add(line.replace(".", "\\\\."))



hostsFile.close()

count = 0

output = open("output.txt", "w")

output.writelines("[\r")

domains = list(domains)



for domain in domains:
    count += 1
    
    s = "{ \"id\":" + str(count) + ",\"priority\":1,\"action\":{\"type\":\"block\"},\"condition\":{\"regexFilter\":\"http(s)?://(.*\\\\.)?" + domain + ".*\",}}"
    
    if domain != domains[-1]:
        s += ","

    s += "\r"
    
    output.writelines(s)



output.writelines("]")

output.close()

print(f"produced {count} domains")
