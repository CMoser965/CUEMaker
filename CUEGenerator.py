# CUEGenerator.py
import os, io

for filename in os.listdir('.'):
    if filename.endswith('.bin'):
        if "Track" in filename:
            
            if "Track" in filename:
                if filename[filename.index("Track ") + 7] != ')':
                    trackval = int(filename[filename.index("Track ") + 6] + filename[filename.index("Track ") + 7])
                else: 
                    trackval = int(filename[filename.index("Track ") + 6])
            # elif "Track 1)" in filename:
            #     trackval = int(filename[filename.index("Track ") + 6])
            if "(Track 1)" in filename or "(Track 01)" in filename:
                cuename = filename[0:filename.index("(Track") - 1] + ".cue"
                print(cuename)
            else:
                print(trackval)
            
            if trackval == 1:
                if(os.path.exists(cuename)):
                    print("Something weird happened (err 01). Skipping. . .")
                    continue
                
                print("Creating CUE file for " + cuename)

                with open(cuename, "w") as cue:
                    cue.writelines(['FILE "' + filename + '" BINARY\n', '\tTRACK 01 MODE2/2352\n\t\tINDEX 01 00:00:00\n'])
            
            else:
                if(not os.path.exists(cuename)):
                    print("Something weird happened (err 02). Skipping . . .")

                print("Added track " + str(trackval) + " to " + cuename)

                with open(cuename, "a") as cue:
                    cue.write('FILE "' + filename + '" BINARY\n')
                    if trackval < 11:
                        cue.write('\tTRACK 0' + str(trackval) + '\n\t\tINDEX 0' + str(trackval) + ' 00:00:00\n')
                    else:
                        cue.write('\tTRACK ' + str(trackval) + '\n\t\tINDEX ' + str(trackval) + ' 00:00:00\n')




print("Done.")
print("        _=====_                               _=====_\n       / _____ \                             / _____ \\\n     +.-'_____'-.---------------------------.-'_____'-.+\n    /   |     |  '.        S O N Y        .'  |  _  |   \\\n   / ___| /|\\ |___ \\                     / ___| /_\\ |___ \\\n  / |      |      | ;  __           _   ; | _         _ | ;\n  | | <---   ---> | | |__|         |_:> | ||_|       (_)| |\n  | |___   |   ___| ;SELECT       START ; |___       ___| ;\n  |\    | \|/ |    /  _     ___      _   \    | (X) |    /|\n  | \   |_____|  .','" "', |___|  ,'" "', '.  |_____|  .' |\n  |  '-.______.-' /       \ANALOG/       \  '-._____.-'   |\n  |               |       |------|       |                |\n  |              /\       /      \       /\               |\n  |             /  '.___.'        '.___.'  \              |\n  |            /                            \             |\n   \          /                              \           /\n    \________/                                \_________/")
print("Let's Play.")