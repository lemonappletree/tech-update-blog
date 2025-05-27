# 🛠️ 2025-05-27 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces the graduation of the "in-place Pod resize" feature to Beta in Kubernetes v1.33, which will be enabled by default. This feature allows for dynamic adjustment of CPU and memory resources in running Pods without needing to restart them, making it particularly beneficial for stateful applications, batch jobs, and sensitive workloads. The move from Alpha to Beta involved significant improvements in stability, user experience, and the addition of support for resizing sidecar containers. The update includes enhancements in resource management, faster resize detection, and improved integration with container runtimes. The community is focusing on further stabilizing the feature, integrating it with the VerticalPodAutoscaler, and gathering user feedback for future enhancements. Users are encouraged to try out the feature and provide feedback through Kubernetes communication channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Repository Vector Search Methods
The blog post discusses the evolution and integration of vector search methods within the Spring ecosystem, highlighting the rise of vector databases driven by Large Language Models (LLM) and their applications in Generative AI. Vector search involves using vector representations of data to efficiently find similar items, commonly applied in Retrieval-Augmented Generation (RAG) systems. The post categorizes databases into dedicated vector databases and general-purpose databases with vector capabilities. It notes how Spring AI supports vector search, simplifying AI integration into Spring applications. The focus then shifts to Spring Data, which now supports vector types with its 3.5 release, and explores vector search methods in Spring Data 4.0 for JPA, MongoDB, and Apache Cassandra. These methods allow repository searches based on vector similarity, enhancing data retrieval processes. The blog emphasizes the importance of vector search in modern data systems and invites feedback for further improvements.
👉 [Read more](https://spring.io/blog/2025/05/23/vector-search-methods)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
The blog post introduces Docker Hardened Images, which are designed to enhance security, ensure minimalism, and be ready for production use. Docker has consistently aimed to help developers build, share, and run software in an efficient and secure manner. With Docker Hub facilitating software delivery on a global scale, featuring over 14 million images and more than 11 billion pulls monthly, Docker has gained significant insights into modern software development. The new Hardened Images are a response to these insights, providing developers with secure and streamlined options for their software projects.
👉 [Read more](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP 510: Key Derivation Function API
The blog post discusses JEP 510, which introduces a new Key Derivation Function (KDF) API targeted for JDK 25. The purpose of this API is to provide a standardized way to derive cryptographic keys from various types of input material, thereby enhancing security and consistency across Java applications. This API aims to simplify the process of key derivation for developers, ensuring they have access to reliable and efficient cryptographic operations. The post likely elaborates on the features and benefits of the new API and its potential impact on Java's cryptographic capabilities.
👉 [Read more](https://inside.java/2025/05/26/jep510-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
The blog post discusses a security audit of Go's cryptographic libraries conducted by Trail of Bits. The audit aimed to evaluate the security and robustness of these libraries, identify potential vulnerabilities, and ensure that they meet high security standards. The results of the audit are intended to enhance the overall security of Go's cryptographic implementations. Further details and findings from the audit can be accessed through the provided link.
👉 [Read more](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025, taking place in London, UK, from April 1 to 4. During the event, the team will discuss the upcoming release of Helm 4 and engage with attendees through various talk sessions and interactions at the Helm booth in the Project Pavilion. The post encourages participants to join these activities to learn more and contribute to the conversation around Helm.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

