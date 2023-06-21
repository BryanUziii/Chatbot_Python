
estrategiasDidacticas = {
    "definicion": "Las estrategias didácticas son técnicas y enfoques utilizados por los docentes para mejorar la enseñanza y el aprendizaje. Estas estrategias involucran actividades prácticas, juegos, proyectos colaborativos y el uso de tecnología para motivar a los estudiantes, fomentar su participación activa y ayudarles a construir conocimientos y habilidades de manera efectiva. El objetivo es crear un entorno de aprendizaje estimulante y enriquecedor que se adapte a las necesidades de los estudiantes.",
    "tipos": {
        "Aprendizaje basado en proyectos": "(ABP) Esta estrategia implica que los estudiantes trabajen en proyectos que les permitan abordar problemas del mundo real. Los proyectos fomentan la investigación, la colaboración, el pensamiento crítico y la creatividad, brindando a los estudiantes una experiencia práctica y significativa.",
        "Aprendizaje cooperativo": "Esta estrategia fomenta la colaboración y el trabajo en equipo. Los estudiantes trabajan juntos para lograr metas comunes, compartiendo conocimientos, habilidades y responsabilidades. El aprendizaje cooperativo promueve la participación activa de todos los estudiantes y el desarrollo de habilidades sociales.",
        "Aprendizaje activo": "Se trata de involucrar activamente a los estudiantes en el proceso de aprendizaje. Los docentes pueden utilizar actividades prácticas, experimentos, debates, juegos de rol y otras técnicas para que los estudiantes se conviertan en protagonistas de su propio aprendizaje. Esto ayuda a mejorar la retención de información y la comprensión de los conceptos.",
        "Aprendizaje basado en problemas": "(ABP) Similar al ABP, esta estrategia se centra en presentar a los estudiantes problemas o situaciones desafiantes para resolver. Los estudiantes deben aplicar sus conocimientos y habilidades para encontrar soluciones, lo que promueve el pensamiento crítico, la resolución de problemas y el aprendizaje autónomo.",
        "Flipped Classroom": "En esta estrategia, los estudiantes adquieren los conceptos teóricos en casa a través de materiales previamente proporcionados, como videos o lecturas. El tiempo en el aula se utiliza para actividades prácticas, discusiones y trabajo colaborativo, permitiendo a los docentes brindar apoyo individualizado.",
        "Diversificación de métodos y recursos": "Es importante que los docentes utilicen una variedad de métodos y recursos didácticos para adaptarse a diferentes estilos de aprendizaje y necesidades de los estudiantes. Esto incluye el uso de multimedia, tecnología educativa, ejemplos concretos, analogías, demostraciones, entre otros."
    }
}

def procesar_entrada(entrada):
    if "tu creador" in entrada or "tus creadores" in entrada:
        return "Fui creado por estudiantes de la UPSIN en 2023"
    
    if "tu nombre" in entrada or "tunombre" in entrada:
        return "Mi nombre es ..:: ChatbotP3 ::.."
    
    if ("tipos" in entrada or "cuales son" in entrada) and ("estrategia" in entrada or "estrategias" in entrada) and ("didactica" in entrada or "didacticas" in entrada):
        tipos_estrategias = estrategiasDidacticas["tipos"]
        respuesta = "Los tipos de estrategias didácticas son:\n\n"
        for tipo, descripcion in tipos_estrategias.items():
            respuesta += f"{tipo.capitalize()}: {descripcion}\n\n"
        return respuesta
    
    if ("significa" in entrada or "definicion" in entrada or "que son" in entrada or "que es" in entrada) and ("estrategia" in entrada or "estrategias" in entrada) and ("didactica" in entrada or "didacticas" in entrada):
        return estrategiasDidacticas["definicion"]
    
    else:
        if "?" in entrada:
            return "No entiendo tu pregunta"
        else:
            return "No entiendo que quieres decir"
        
