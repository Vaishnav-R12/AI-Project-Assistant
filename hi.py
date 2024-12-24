import streamlit as st
from hello import generate_project_tasks, get_next_step, generate_readme

def main():
    st.title("AI Project Assistant")
    
    # Sidebar for Project Type Selection
    project_type = st.sidebar.selectbox(
        "Select Project Type", 
        ["Web Development", "Machine Learning", "Mobile App Development"]
    )
    
    # Display project tasks
    st.subheader(f"Tasks for {project_type}")
    tasks = generate_project_tasks(project_type)
    completed_tasks = []
    
    # Create checkboxes for tasks
    for task in tasks:
        if st.checkbox(task):
            completed_tasks.append(task)
    
    # Suggest next step
    if completed_tasks:
        next_step = get_next_step(completed_tasks)
        st.write(next_step)
    
    # Display Documentation Template
    st.subheader("Generate Project Documentation (README)")
    readme = generate_readme(project_type)
    st.text_area("Generated README", readme, height=300)
    
    # Option to download the README as a file
    if st.button("Download README"):
        with open(f"{project_type}_README.txt", "w") as f:
            f.write(readme)
        st.success("README file has been generated!")

if __name__ == "__main__":
    main()
