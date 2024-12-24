def generate_project_tasks(project_type):
    tasks = {
        "Web Development": [
            "Set up project structure",
            "Install necessary libraries",
            "Create basic homepage",
            "Set up database",
            "Deploy application"
        ],
        "Machine Learning": [
            "Data collection and preprocessing",
            "Feature selection",
            "Model selection",
            "Model training",
            "Model evaluation",
            "Deploy model"
        ],
        "Mobile App Development": [
            "Design UI",
            "Set up API endpoints",
            "Implement app logic",
            "Integrate with database",
            "Deploy app"
        ]
    }
    return tasks.get(project_type, [])
def get_next_step(completed_tasks):
    all_tasks = [
        "Set up project structure", "Install necessary libraries", "Create basic homepage",
        "Set up database", "Deploy application", "Data collection and preprocessing",
        "Feature selection", "Model selection", "Model training", "Model evaluation",
        "Deploy model", "Design UI", "Set up API endpoints", "Implement app logic",
        "Integrate with database", "Deploy app"
    ]
    remaining_tasks = [task for task in all_tasks if task not in completed_tasks]
    if remaining_tasks:
        return f"Next step: {remaining_tasks[0]}"
    return "All tasks are complete!"
def generate_readme(project_type):
    readme_templates = {
        "Web Development": """
        # Web Development Project
        ## Project Overview
        Brief description of the web app.

        ## Technologies Used
        - HTML, CSS, JavaScript
        - Flask/Django
        - SQL

        ## Installation
        Steps to install and run the project.

        ## Usage
        Instructions to use the app.
        """,
        "Machine Learning": """
        # Machine Learning Project
        ## Project Overview
        Description of the ML model and its purpose.

        ## Technologies Used
        - Python
        - TensorFlow/PyTorch
        - scikit-learn

        ## Installation
        Steps to install and run the project.

        ## Usage
        Instructions on how to train and evaluate the model.
        """,
        "Mobile App Development": """
        # Mobile App Development Project
        ## Project Overview
        A brief description of the mobile app.

        ## Technologies Used
        - React Native / Flutter
        - Firebase / SQLite

        ## Installation
        Steps to install and run the app.

        ## Usage
        Instructions on how to use the app.
        """
    }
    return readme_templates.get(project_type, "No template available.")
