import difflib
from pickle import FALSE

estrategiasDidacticas = {
    "definicion": "Las estrategias didácticas son técnicas y enfoques utilizados por los docentes para mejorar la enseñanza y el aprendizaje. Estas estrategias involucran actividades prácticas, juegos, proyectos colaborativos y el uso de tecnología para motivar a los estudiantes, fomentar su participación activa y ayudarles a construir conocimientos y habilidades de manera efectiva. El objetivo es crear un entorno de aprendizaje estimulante y enriquecedor que se adapte a las necesidades de los estudiantes.",
   
    "importancia": """Las estrategias didácticas son importantes o sirven para:\n
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
        
    "como_aplicarlas": """Para que sea realmente eficaz, una estrategia didáctica requiere de una planificación y organización previa que, como mínimo, abarque los siguientes aspectos:\n
        1.- Especificar los objetivos concretos que se pretenden conseguir con una determinada materia o aprendizaje.
        2.- Recopilar y preparar toda la información, materiales, dispositivos u objetos necesarios en la explicación y enseñanza de dicha materia.
        3.- Asociar los conocimientos teóricos a experimentos o actividades con un enfoque práctico.
        4.- Encontrar maneras de enfatizar y remarcar los aspectos más importantes que se quieren enseñar o transmitir.
        5.- Fomentar la autonomía del alumnado.
        6.- Potenciar la implicación del alumnado en las clases, fomentando su participación.""",
        
    "cuando_aplicarlas": """Las estrategias didácticas pueden ser utilizadas en diversos contextos educativos y situaciones de enseñanza. Su aplicación no se limita únicamente al aula tradicional, sino que también pueden ser utilizadas en otros entornos educativos y formatos de aprendizaje. A continuación, se presentan algunos momentos y situaciones en los cuales se pueden utilizar las estrategias didácticas: \n
        1.- En el aula escolar: Las estrategias didácticas son comúnmente utilizadas por docentes en el aula para enseñar diferentes materias y contenidos curriculares. Pueden aplicarse en todos los niveles educativos, desde preescolar hasta la educación superior.
        2.- Formación y capacitación: En el ámbito de la formación profesional, las estrategias didácticas se utilizan para impartir cursos y talleres que buscan desarrollar habilidades específicas en los participantes.
        3.- Educación en línea: Las estrategias didácticas también son aplicables en la educación en línea o a distancia. Los educadores pueden utilizar recursos multimedia, foros de discusión, actividades interactivas y otras técnicas para promover el aprendizaje en línea.
        4.- Seminarios y conferencias: Los presentadores y conferenciantes pueden emplear estrategias didácticas para mantener el interés del público, fomentar la participación y asegurar que los asistentes retengan la información clave.
        5.- Talleres y actividades extraescolares: En eventos extraescolares o talleres educativos, las estrategias didácticas pueden utilizarse para promover la colaboración entre los participantes y lograr una comprensión más profunda de los temas tratados.
        6.- Educación no formal: En contextos de educación no formal, como programas de educación comunitaria o proyectos de alfabetización, las estrategias didácticas pueden ser útiles para adaptar el aprendizaje a las necesidades específicas de los participantes.
        7.- Educación para adultos: En programas de educación para adultos, las estrategias didácticas se utilizan para involucrar a los estudiantes en su proceso de aprendizaje y fomentar un ambiente propicio para el desarrollo de nuevas habilidades.
        8.- Actividades de divulgación y concientización: En eventos de divulgación y concientización sobre temas específicos (por ejemplo, salud, medio ambiente, derechos humanos), las estrategias didácticas pueden ayudar a transmitir información de manera efectiva.
    """,
        
    "beneficios": """Algunos de los beneficios más destacados de las estrategias didácticas incluyen:\n
        1.- Mejora del aprendizaje: Las estrategias didácticas están diseñadas para promover una comprensión más profunda y significativa del contenido por parte de los estudiantes, lo que resulta en un aprendizaje más efectivo.
        2.- Mayor motivación: Al utilizar métodos didácticos variados y estimulantes, los estudiantes pueden sentirse más motivados para participar activamente en el proceso de aprendizaje.
        3.- Adaptación a estilos de aprendizaje: Las estrategias didácticas pueden adaptarse a diferentes estilos de aprendizaje, lo que permite a los educadores satisfacer las necesidades individuales de los estudiantes.
        4.- Promoción de la retención a largo plazo: Al incorporar técnicas como la repetición espaciada, el aprendizaje basado en la resolución de problemas y la conexión con conocimientos previos, las estrategias didácticas ayudan a los estudiantes a retener la información durante más tiempo.
        5.- Fomento del pensamiento crítico: Al utilizar enfoques como el aprendizaje activo y el debate, las estrategias didácticas estimulan el pensamiento crítico y la capacidad de análisis de los estudiantes.
        6.- Facilitación de la participación activa: Las estrategias didácticas promueven la participación activa de los estudiantes en el proceso de aprendizaje, lo que les permite construir su conocimiento y habilidades de manera más efectiva.
        7.- Reducción del aburrimiento: Al diversificar la forma en que se presenta la información, las estrategias didácticas pueden ayudar a reducir el aburrimiento y mantener el interés de los estudiantes en el contenido.
        8.- Fortalecimiento del trabajo en equipo y la colaboración: Algunas estrategias didácticas fomentan el trabajo en equipo y la colaboración entre los estudiantes, lo que les permite aprender de manera cooperativa y mejorar sus habilidades sociales.
        9.- Personalización del aprendizaje: Al adaptar las estrategias didácticas según las necesidades individuales de los estudiantes, se puede lograr un aprendizaje más personalizado y efectivo.
        10.- Mejora del ambiente de aprendizaje: El uso adecuado de estrategias didácticas puede crear un ambiente de aprendizaje más dinámico, interactivo y enriquecedor para los estudiantes.""",
    
    "caracteristicas": """Las estrategias didácticas comparten diversas características que las hacen efectivas para facilitar el proceso de enseñanza y aprendizaje. A continuación, se presentan algunas de las principales características de las estrategias didácticas:\n
        1.- Intencionalidad educativa: Las estrategias didácticas están diseñadas con un propósito educativo claro. Cada estrategia tiene objetivos específicos que se alinean con los resultados de aprendizaje deseados.\n
        2.- Flexibilidad: Las estrategias didácticas pueden adaptarse a diferentes contextos educativos y a las necesidades particulares de los estudiantes. Los educadores pueden ajustarlas para que se ajusten mejor al grupo o individuo al que están enseñando.\n
        3.- Enfoque en el estudiante: Las estrategias didácticas ponen énfasis en el estudiante como el protagonista del proceso de aprendizaje. Están diseñadas para involucrar activamente a los estudiantes en la construcción de su propio conocimiento.\n
        4.- Aprendizaje significativo: Buscan promover el aprendizaje significativo, donde los estudiantes relacionen los nuevos conocimientos con sus experiencias previas y comprendan su relevancia en su vida cotidiana.\n
        5.- Variedad y diversidad: Las estrategias didácticas abarcan una amplia gama de técnicas y métodos pedagógicos. Esta diversidad permite abordar diferentes estilos de aprendizaje y mantener el interés de los estudiantes.\n
        6.- Promoción de la participación activa: Fomentan la participación activa de los estudiantes en el proceso educativo. Esto implica que los estudiantes se involucren en debates, discusiones, actividades prácticas y otros tipos de interacción.\n
        7.- Estimulación de la curiosidad y el pensamiento crítico: Las estrategias didácticas buscan estimular la curiosidad de los estudiantes y fomentar el pensamiento crítico y analítico, para que puedan cuestionar, investigar y comprender más profundamente los temas tratados.\n
        8.- Evaluación integrada: Las estrategias didácticas incluyen métodos para evaluar el progreso de los estudiantes y asegurar que los objetivos de aprendizaje se estén cumpliendo. La evaluación se integra de manera coherente con las actividades de enseñanza.\n
        9.- Apoyo al aprendizaje autónomo: Se busca que los estudiantes adquieran habilidades para el aprendizaje autónomo, para que puedan seguir aprendiendo de manera independiente más allá del aula.\n
        10.- Uso de recursos tecnológicos y multimedia: Las estrategias didácticas pueden incorporar recursos tecnológicos y multimedia, como presentaciones interactivas, videos educativos o plataformas de aprendizaje en línea, para enriquecer la experiencia educativa.""",
            
    "ventajas": """Ventajas de utilizar estrategias didácticas:\n
        1.- Promueven la participación activa: Las estrategias didácticas bien diseñadas fomentan la participación activa de los estudiantes en el proceso de aprendizaje, lo que puede mejorar su compromiso y motivación.
        2.- Favorecen el aprendizaje significativo: Al adaptarse a los estilos y ritmos de aprendizaje de los estudiantes, estas estrategias pueden ayudar a construir conexiones significativas con los conocimientos previos y facilitar la retención a largo plazo.
        3.- Facilitan la comprensión: Las estrategias didácticas pueden ayudar a explicar conceptos difíciles de manera más clara y accesible para los estudiantes, facilitando la comprensión de temas complejos.
        4.- Estimulan la creatividad y el pensamiento crítico: Al utilizar enfoques interactivos y participativos, las estrategias didácticas pueden estimular la creatividad y el pensamiento crítico de los estudiantes, ayudándolos a desarrollar habilidades analíticas.
        5.- Adaptabilidad: Existen diversas estrategias didácticas, lo que permite a los educadores adaptar su enfoque según las necesidades y características específicas de sus estudiantes.""",
     
    "desventajas": """Desventajas de utilizar estrategias didácticas:\n
        1.- Requieren tiempo y planificación: Algunas estrategias didácticas pueden demandar más tiempo y preparación por parte de los educadores, lo que puede ser un desafío en entornos con recursos limitados.
        2.- Necesitan recursos adecuados: Algunas estrategias didácticas pueden requerir recursos específicos, como tecnología, materiales educativos, espacios adecuados, etc., lo que puede ser un obstáculo en ciertos contextos educativos.
        3.- Resistencia al cambio: Algunos educadores y estudiantes pueden resistirse a nuevas estrategias didácticas, especialmente si difieren significativamente de los métodos tradicionales de enseñanza.
        4.- Evaluación y seguimiento: Es importante evaluar y hacer un seguimiento del impacto de las estrategias didácticas en el aprendizaje de los estudiantes para garantizar que estén funcionando de manera efectiva.
        5.- Adaptabilidad: Si bien la adaptabilidad es una ventaja, también puede ser una desventaja si las estrategias no se ajustan correctamente a las necesidades y estilos de aprendizaje de los estudiantes, lo que podría llevar a una experiencia educativa menos efectiva.""",
    
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
        
        if "significa" in entrada or "definicion" in entrada or "que son" in entrada or "que es una" in entrada or "concepto" in entrada:
            return estrategiasDidacticas["definicion"]      
            
        if "tipo" in entrada or "ejemplo" in entrada:
            tipos_estrategias = estrategiasDidacticas["tipos"]
            respuesta = "Los tipos de estrategias didácticas son:\n\n"
            for tipo, estrategia in tipos_estrategias.items():
                descripcion = estrategia["descripcion"]
                ejemplo = estrategia["ejemplo"]
                respuesta += f"{tipo.capitalize()}: {descripcion}\nEjemplo de aplicación: {ejemplo}\n\n"
            return respuesta
        
        if "benefi" in entrada:
            return estrategiasDidacticas["beneficios"]
        
        if "ventaja" in entrada or "desventaja" in entrada:
            if "ventaja" in entrada and "y" in entrada and "desventaja" in entrada:
                return "" + estrategiasDidacticas["ventajas"] + "\n\n" + estrategiasDidacticas["desventajas"]
            
            if "desventaja" in entrada:
                return estrategiasDidacticas["desventajas"]
              
            if "ventaja" in entrada:
                return estrategiasDidacticas["ventajas"]
             
        if "importan" in entrada or "sirve" in entrada:
            return estrategiasDidacticas["importancia"]
        
        if "aplicar" in entrada or "utiliza" in entrada:
            if "cuando" in entrada:
                return estrategiasDidacticas["cuando_aplicarlas"]
            if "como" in entrada:
                return estrategiasDidacticas["como_aplicarlas"]
        
        if "objetivo" in entrada or "proposito" in entrada:
            return estrategiasDidacticas["objetivo"]
        
        if "caracteristica" in entrada:
            return estrategiasDidacticas["caracteristicas"]
    
    if "tu creador" in entrada or "tus creadores" in entrada or "quien te creo" in entrada:
        return "Fui creado por estudiantes de la UPSIN en 2023"
    
    if "tu nombre" in entrada or "tunombre" in entrada:
        return "Mi nombre es Chatbot"
    
    if "hola" in entrada or "saludos" in entrada:
        return "Hola compañerine."
    
    if "?" in entrada:
        return "No entiendo tu pregunta"
    
    return "No entiendo que quieres decir"

