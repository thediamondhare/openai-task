
from openai_client import  generatePrompt
from reading_article import readArticleContent
                

schemaPrompt = """
Produce a single page website template with blank body. That website should be an HTML file with embedded javascript and CSS.
""".strip()
def main():
        
    try:
        articleText = readArticleContent()

        articlePrompt = """
        Produce a single page website body content with article according five guidelines listed below:
        Guidelines:
        1. This should be an HTML file.
        2. The content should contain an article text: """ + articleText +""" 
        3. An article mentioned before should be splitted into paragraphs.
        4. Choose where in the article mentioned before it's worth to place an image or images and create there the <img> tag with attribute src="image_placeholder.jpg" and for the every <img> tag choose content of an alt attribute which would be needed for generating the suitable image with openai.

        """.strip()
        

        articleHtml = generatePrompt(articlePrompt)

        if not isinstance(articleHtml, str): 
            articleHtml = str(articleHtml)

        with open('artykul.html', 'w', encoding='utf-8') as file: 
            file.write(articleHtml)
    except:
        raise ValueError
        

    try:

        schemaHtml = generatePrompt(schemaPrompt)

        if not isinstance(schemaHtml, str): 
            schemaHtml = str(schemaHtml)

        with open('szablon.html', 'w', encoding='utf-8') as file: 
            file.write(schemaHtml)
    except:
        raise ValueError

if __name__ == "__main__":
    main()
