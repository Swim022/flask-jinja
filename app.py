
from flask import Flask, render_template, request
from stories import story  # Import the story from stories.py

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage: Shows the form to fill out Madlib words."""
    prompts = story.prompts  # Get the prompts from the story
    return render_template("home.html", prompts=prompts)  # Render the form

@app.route('/story')
def show_story():
    """Story page: Display the generated Madlib story."""
    # Collect answers from the form
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    
    # Generate the story using the answers
    generated_story = story.generate(answers)
    
    # Render the story page
    return render_template("story.html", story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
