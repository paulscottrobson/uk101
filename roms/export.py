#
#		ROM exporter
#
import os

def export(sourceFile,targetFile):
	romImage = [x for x in open(sourceFile,"rb").read(-1)]
	print("Exporting {0} ({1} bytes)".format(sourceFile,len(romImage)))
	h = open(targetFile,"w")
	romImage = ",".join([str(x) for x in romImage])
	romImage = "{ "+romImage+" }"
	arrayName = targetFile.replace(".inc","").split(os.sep)[-1]
	h.write("static const BYTE8 {0}[] = {1} ;\n\n".format(arrayName,romImage))
	h.close()

export("basic.rom","../emulator/basic_rom.inc")
export("character.rom","../emulator/character_rom.inc")
#export("monitor.rom","../emulator/monitor_rom.inc")
#export("monitor-2.rom","../emulator/monitor_rom.inc")
export("cegmon.rom","../emulator/monitor_rom.inc")
