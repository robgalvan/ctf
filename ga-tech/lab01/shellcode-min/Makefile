ASFLAGS += -m64
CFLAGS  += -m64 -g -O0 -std=c99 -Wall -Werror -fno-stack-protector -z execstack

ALL := readflag.bin

all: $(ALL)

%.bin: %.o
	objcopy -S -O binary -j .text $< $@

clean:
	rm -f *.bin

.PHONY: all clean