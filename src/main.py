from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil
from functions import copy_files_recursive, generate_pages_recursive
        
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive("./content/", "template.html", "./public/")


main()