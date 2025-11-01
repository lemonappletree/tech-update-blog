# 🛠️ 2025-11-01 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post discusses seven common pitfalls in Kubernetes usage and provides tips on how to avoid them. The author shares personal experiences with these issues, aiming to help readers, whether they are new to Kubernetes or managing production clusters, avoid similar mistakes. The pitfalls include: 

1. **Skipping Resource Requests and Limits**: Not setting CPU and memory requirements can lead to resource starvation or hoarding.
2. **Underestimating Liveness and Readiness Probes**: Failing to define health checks can cause issues if a container is unresponsive or not ready.
3. **Relying Solely on Container Logs**: Using only `kubectl logs` can lead to lost logs, so centralizing logs is recommended.
4. **Treating Dev and Prod the Same**: Using identical settings across environments can lead to instability; customization is crucial.
5. **Leaving Old Resources Around**: Forgotten resources can consume resources and increase costs, so regular audits and labeling are important.
6. **Diving Too Deep into Networking Too Soon**: Advanced networking solutions should only be added once core networking is understood.
7. **Going Too Light on Security and RBAC**: Insecure configurations pose risks; using RBAC and security policies is essential.

The post concludes by emphasizing the importance of understanding Kubernetes deeply and learning from mistakes to improve cluster management.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
The blog post announces the release of Spring Data 2025.1.0-RC2, the second release candidate for the upcoming Spring Data generation. This release incorporates updates from Spring Framework RC3 and Spring HATEOAS RC2 and includes refinements and structural cleanups in Spring Data Commons. The post also mentions plans to release Spring Data 2025.1 GA in mid-November, in coordination with the forthcoming Spring Framework 7.0 release. It provides links to the Javadoc, documentation, and changelogs for various Spring Data projects, such as Spring Data JPA, MongoDB, Neo4j, and others. More details can be found in the linked release notes.
👉 [Read more](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
The blog post titled "Security Doesn’t Have to Hurt" discusses the common frustration of security measures blocking necessary tools, such as AI services for translating documentation. It highlights that security teams also wish for smoother processes and not to hinder productivity. The post suggests that collaboration between security and IT departments can help balance security needs with accessibility, ensuring that necessary tools are available without compromising security. By working together, organizations can find solutions that allow employees to efficiently complete their work while maintaining robust security protocols.
👉 [Read more](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS
In the blog post titled "Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS," the author discusses the evolution of Project Valhalla's approach to flattening value types. The changes are influenced by a better understanding of the semantics of value types and the challenges faced within the Java language and the Java Virtual Machine (JVM). The post likely explores the implications and expected outcomes of these advancements in the context of JEP 401, providing insights into how they could impact Java development and performance.
👉 [Read more](https://inside.java/2025/10/31/jvmls-jep-401/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector called "Green Tea" in Go version 1.25. This innovation aims to enhance memory management efficiency in the Go programming language. The Green Tea garbage collector is designed to improve performance by optimizing memory usage and reducing latency, providing developers with a more efficient tool for managing memory in their applications. The blog post likely elaborates on the technical details, benefits, and potential impacts of this new garbage collector within the Go ecosystem.
👉 [Read more](https://go.dev/blog/greenteagc)

