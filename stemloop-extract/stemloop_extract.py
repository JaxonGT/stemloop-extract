import os, sys

path = "."

for file in os.listdir(path):
    if file.endswith(".txt"):

        lines = []
        headers = []
        loops = []
        stems = []

        f = open(file, "r")
        for line in f:
            if line.startswith(">"):
                headers.append(line)
            else:
                lines.append(line)

        f.close()

        for i in range(len(lines[0])):
            for j in range(len(lines)):
                if i == 0:
                    loops.append("")
                    stems.append("")

                if "." in lines[0][i]:
                    loops[j] = loops[j] + lines[j][i]
                elif "\n" in lines[0][i]:
                    loops[j] = loops[j] + lines[j][i]
                    stems[j] = stems[j] + lines[j][i]
                else:
                    stems[j] = stems[j] + lines[j][i]
                    
        floop = open(file.replace(".txt","_loop.txt"), "w")
        fstem = open(file.replace(".txt","_stem.txt"), "w")

        for k in range(1,len(headers)):
            floop.write(headers[k])
            fstem.write(headers[k])
            floop.write(loops[k])
            fstem.write(stems[k])
            
        floop.close()
        fstem.close()