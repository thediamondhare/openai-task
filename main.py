from openai_client import generatePrompt
from reading_article import readArticleContent
                
defaultSystemInputForArticle = """
Produce a single page website body content according five guidelines listed below:
# Guidelines
1. The file should be an HTML file.
2. The content should contain an article in Polish language created by text template given in the current prompt.
3. An article mentioned before should be splitted into paragraphs.
4. Choose where in the article mentioned before it's worth to place an image or images and create there the <img> tag with attribute src="image_placeholder.jpg" and for the every <img> tag choose content of an alt attribute which would be needed for generating the suitable image with openai.

""".strip()

defaultSystemInputForTemplate = """
Produce a single page website template with blank body. That website should be an HTML file with embedded javascript and CSS.
""".strip()

defaultUserInput = readArticleContent()

articleHtml = generatePrompt(defaultSystemInputForArticle, defaultUserInput)

with open('artykul.html', 'w', encoding='utf-8') as file: 
    file.write(articleHtml)

#schemaHtml = generatePrompt(defaultSystemInputForTemplate, defaultUserInput)

#with open('szablon.html', 'w', encoding='utf-8') as file: 
#    file.write(schemaHtml)
