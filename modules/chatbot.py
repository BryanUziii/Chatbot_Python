import difflib
from pickle import FALSE

estrategiasDidacticas = {
    "definicion": "Las estrategias didácticas son técnicas y enfoques utilizados por los docentes para mejorar la enseñanza y el aprendizaje. Estas estrategias involucran actividades prácticas, juegos, proyectos colaborativos y el uso de tecnología para motivar a los estudiantes, fomentar su participación activa y ayudarles a construir conocimientos y habilidades de manera efectiva. El objetivo es crear un entorno de aprendizaje estimulante y enriquecedor que se adapte a las necesidades de los estudiantes.",
    "importancia": """Las estrategias didácticas son importantes porque:\n
        1.- Facilitan el aprendizaje al ayudar a los estudiantes a comprender y retener la información.
        2.- Promueven la participación activa de los estudiantes en el proceso de aprendizaje.
        3.- Se adaptan a las necesidades y características de los estudiantes.
        4.- Estimulan la motivación y el interés por aprender.
        5.- Mejoran la retención de conocimientos al fomentar el aprendizaje significativo.""",
    "objetivo": """Los objetivos principales de utilizar estrategias didácticas en el aula son los siguientes:\n
        1.- Promover el aprendizaje activo y significativo: Las estrategias didácticas buscan involucrar a los estudiantes de manera activa en el proceso de aprendizaje, fomentando su participación, reflexión y construcción de conocimientos. El objetivo es que los estudiantes no sean meros receptores pasivos de información, sino que sean participantes activos en su propio aprendizaje.\n
        2.- Mejorar la comprensión y retención de los contenidos: Las estrategias didácticas están diseñadas para ayudar a los estudiantes a comprender y retener los contenidos de manera más efectiva. Estas estrategias utilizan técnicas como la ejemplificación, la práctica, la aplicación y la conexión con conocimientos previos para facilitar la asimilación y retención de la información.\n
        3.- Estimular el pensamiento crítico y la resolución de problemas: Las estrategias didácticas promueven el desarrollo del pensamiento crítico y la capacidad de resolver problemas en los estudiantes. Estas estrategias incluyen actividades que requieren análisis, evaluación, argumentación y toma de decisiones, lo que ayuda a desarrollar habilidades cognitivas superiores.\n
        4.- Atender a la diversidad de los estudiantes: Las estrategias didácticas se adaptan a las necesidades y características individuales de los estudiantes, considerando su diversidad en términos de estilos de aprendizaje, habilidades, intereses y ritmos de aprendizaje. El objetivo es proporcionar un entorno inclusivo y equitativo que permita a todos los estudiantes alcanzar los objetivos de aprendizaje.\n
        5.- Fomentar la motivación y el interés por aprender: Las estrategias didácticas buscan mantener la motivación y el interés de los estudiantes en el proceso de aprendizaje. Utilizan métodos variados, recursos multimedia, actividades interactivas y desafíos intelectuales para generar un ambiente estimulante y atractivo que motive a los estudiantes a participar y aprender de manera activa.""",
    "tipos": {
        "Aprendizaje basado en proyectos": {
            "descripcion": "(ABP) Esta estrategia implica que los estudiantes trabajen en proyectos que les permitan abordar problemas del mundo real. Los proyectos fomentan la investigación, la colaboración, el pensamiento crítico y la creatividad, brindando a los estudiantes una experiencia práctica y significativa.",
            "ejemplo": "Los estudiantes trabajan en un proyecto para diseñar y construir un modelo de energía renovable."
        },
        "Aprendizaje cooperativo": {
            "descripcion": "Esta estrategia fomenta la colaboración y el trabajo en equipo. Los estudiantes trabajan juntos para lograr metas comunes, compartiendo conocimientos, habilidades y responsabilidades. El aprendizaje cooperativo promueve la participación activa de todos los estudiantes y el desarrollo de habilidades sociales.",
            "ejemplo": "Ejemplo de aplicación: Los estudiantes forman grupos y colaboran en la resolución de problemas matemáticos complejos."
        },
        "Aprendizaje activo": {
            "descripcion": "Se trata de involucrar activamente a los estudiantes en el proceso de aprendizaje. Los docentes pueden utilizar actividades prácticas, experimentos, debates, juegos de rol y otras técnicas para que los estudiantes se conviertan en protagonistas de su propio aprendizaje. Esto ayuda a mejorar la retención de información y la comprensión de los conceptos.",
            "ejemplo": "Los estudiantes participan activamente en actividades prácticas para adquirir conocimientos."
        },
        "Aprendizaje basado en problemas": {
            "descripcion": "(ABP) Similar al ABP, esta estrategia se centra en presentar a los estudiantes problemas o situaciones desafiantes para resolver. Los estudiantes deben aplicar sus conocimientos y habilidades para encontrar soluciones, lo que promueve el pensamiento crítico, la resolución de problemas y el aprendizaje autónomo.",
            "ejemplo": "Los estudiantes investigan y resuelven un problema de la vida real relacionado con el medio ambiente."
        },
        "Flipped Classroom": {
            "descripcion": "En esta estrategia, los estudiantes adquieren los conceptos teóricos en casa a través de materiales previamente proporcionados, como videos o lecturas. El tiempo en el aula se utiliza para actividades prácticas, discusiones y trabajo colaborativo, permitiendo a los docentes brindar apoyo individualizado.",
            "ejemplo": "Los estudiantes ven un video explicativo en casa y luego participan en actividades de resolución de problemas en el aula."
        },
        "Diversificación de métodos y recursos": {
            "descripcion": "Es importante que los docentes utilicen una variedad de métodos y recursos didácticos para adaptarse a diferentes estilos de aprendizaje y necesidades de los estudiantes. Esto incluye el uso de multimedia, tecnología educativa, ejemplos concretos, analogías, demostraciones, entre otros.",
            "ejemplo": "Los docentes utilizan una combinación de videos, presentaciones interactivas y actividades prácticas para enseñar un concepto complejo."
        }
    }
}


def procesar_entrada(entrada):
    
    if ("estrategia" in entrada or "estrategias" in entrada) and ("didactica" in entrada or "didacticas" in entrada):
        
        if "significa" in entrada or "definicion" in entrada or "que son" in entrada or "que es" in entrada or "concepto" in entrada:
            return estrategiasDidacticas["definicion"]
        
        if "tipos" in entrada or "cuales son" in entrada or "ejemplo" in entrada:
            tipos_estrategias = estrategiasDidacticas["tipos"]
            respuesta = "Los tipos de estrategias didácticas son:\n\n"
            for tipo, estrategia in tipos_estrategias.items():
                descripcion = estrategia["descripcion"]
                ejemplo = estrategia["ejemplo"]
                respuesta += f"{tipo.capitalize()}: {descripcion}\nEjemplo de aplicación: {ejemplo}\n\n"
            return respuesta
        
        if "importancia" in entrada:
            return estrategiasDidacticas["importancia"]
        
        if "objetivo" in entrada:
            return estrategiasDidacticas["objetivo"]
        
        
        return "jotillo."
    
    if "tu creador" in entrada or "tus creadores" in entrada:
        return "Fui creado por estudiantes de la UPSIN en 2023"
    
    if "tu nombre" in entrada or "tunombre" in entrada:
        return "Mi nombre es Chatbot"
    
    if "hola" in entrada or "saludos" in entrada:
        return "Hola compañerine."
    
    if "?" in entrada:
        return "No entiendo tu pregunta"
    
    return "No entiendo que quieres decir"

