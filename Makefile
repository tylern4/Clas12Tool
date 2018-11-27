all:
	@make lz4 -C Lz4
	@make -j2 -C Hipo
	@make -j2 -C Banks
	@make -j2 -C Utils

clean:
	@make clean -C Lz4
	@make clean -C Hipo
	@make clean -C Banks
	@make clean -C Utils
	@rm -rf lib/*
