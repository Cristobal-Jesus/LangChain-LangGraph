from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama


load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    information = """Elon Musk es un empresario, inversor y magnate de la tecnología nacido en Sudáfrica, con nacionalidad canadiense y estadounidense. Es reconocido mundialmente por fundar y dirigir empresas revolucionarias como Tesla, dedicada a los vehículos eléctricos; SpaceX, enfocada en la exploración espacial; Starlink, que provee internet satelital; y X, la red social anteriormente llamada Twitter. También lidera firmas de vanguardia como xAI en el sector de la inteligencia artificial, Neuralink en neurotecnología y The Boring Company en la construcción de túneles de transporte masivo. Actualmente está consolidado como la persona más rica del mundo y su enorme influencia abarca tanto la innovación tecnológica global como la participación directa en la política gubernamental de Estados Unidos."""
    
    summary_template = """
    Dame información {information} sobre una persona que quiero crear:
    1. Un pequeño resumen
    2. Dos hechos interesantes sobre él
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    
    #llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-3.6-flash")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    
    print("Resumen generado:")
    print(response.content)


if __name__ == "__main__":
    main()
