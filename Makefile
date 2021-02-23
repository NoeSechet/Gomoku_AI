NAME = pbrain-gomoku-ai

all: $(NAME)

$(NAME):
	cp main.py $(NAME)
	chmod 755 $(NAME)

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf pbrain-gomoku-ai.exe.spec

fclean: clean
	rm -rf pbrain-gomoku-ai
	rm -rf pbrain-gomoku-ai.exe

re: fclean all