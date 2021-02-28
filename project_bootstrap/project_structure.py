
def project_structure(project_name, author, author_email, description):

    ignore = {
        "type": "file",
        "name": "ignore.txt",
        "contents": "ignore this file",
    }

    project_config = {
        "gitignore": {
            "type": "file",
            "name": ".gitignore",
            "contents": "gitignore"
        },
        "readme": {
            "type": "file",
            "name": "README.md",
            "contents": "# README",
        },
        "requirements": {
            "type": "file",
            "name": "requirements.txt",
            "contents": "# add packages in here",
        },
        "data": {
            "type": "folder",
            "name": "data",
            "files": {
                "ignore": ignore
            }
        },
        "docs": {
            "type": "folder",
            "name": "docs",
            "files": {
                "ignore": ignore
            }
        },
        "analysis": {
            "type": "folder",
            "name": "analysis",
            "files": {
                "ignore": ignore
            }
        },
        project_name: {
            "type": "folder",
            "name": project_name,
            "files": {
                "init": {
                    "type": "file",
                    "name": "__init__.py",
                    "contents": "# init"
                }
            }
        },
        "setup": {
            "type": "file",
            "name": "setup.py",
            "contents": "setup",
            "args": {
                "package_name": project_name,
                "author": author,
                "author_email": author_email,
                "description": description
            }     
        }
    }

    return project_config