import git
import os

repo = git.Repo(os.getcwd())
file_to_edit = "testfile.txt"
file_path = os.path.join(os.getcwd(), file_to_edit)

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("Andrew")

with open(file_path, "r") as file:
    content = file.read().replace("Andrew", "Christiano")

with open(file_path, "w") as file:
    file.write(content)

repo.index.add([file_path])
repo.index.commit("Replaced Andrew with Christiano")
repo.remote(name="origin").push()

print("Changes pushed to GitHub.")
