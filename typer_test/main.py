import typer

app = typer.Typer()


@app.command()
def hello(name: str, bool = True):
    print(f"Hello {name}")

@app.command()
def goodbye():
    print("Goodbye")


if __name__ == "__main__":
    app()