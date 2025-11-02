# 🛠️ 2025-11-02 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post titled "7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)" explores common mistakes users make when working with Kubernetes and offers solutions to avoid them. The author shares personal experiences and insights on seven pitfalls:

1. **Skipping Resource Requests and Limits**: Not setting CPU and memory requirements can lead to resource contention or hoarding. The solution is to start with modest resource requests and adjust based on real-world usage.

2. **Underestimating Liveness and Readiness Probes**: Not defining health checks can result in unresponsive containers. It's important to implement simple liveness and readiness probes to ensure application health.

3. **Relying Solely on Container Logs**: Depending only on `kubectl logs` can lead to data loss. Centralizing logs using tools like Fluentd and adopting OpenTelemetry can help preserve log data.

4. **Treating Dev and Prod the Same**: Identical settings across environments can lead to instability. Customizing configurations for each environment is crucial.

5. **Leaving Old Resources Floating Around**: Unused resources can clutter the cluster and incur costs. Regular audits and using labels can help manage resources effectively.

6. **Diving Too Deep into Networking Too Soon**: Implementing advanced networking solutions prematurely can complicate troubleshooting. It's advised to start small and expand as needed.

7. **Going Too Light on Security and RBAC**: Insecure configurations can expose clusters to risks. Implementing RBAC and securing image versions are recommended for better security.

The author concludes by emphasizing the importance of learning from mistakes and utilizing resources like official documentation and community support for ongoing learning.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
The blog post announces the release of the second release candidate (RC2) for the upcoming Spring Data 2025.1.0 version. This release includes updates from Spring Framework RC3 and Spring HATEOAS RC2, with a focus on refinements and structural cleanups within Spring Data Commons. The complete changelog is available in the release notes. The general availability (GA) release for Spring Data 2025.1 is scheduled for mid-November, aligning with the Spring Framework 7.0 release. The post also provides links to the Javadoc, documentation, and changelogs for various Spring Data modules, including JPA, MongoDB, Neo4j, and others.
👉 [Read more](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
The blog post titled "Security Doesn’t Have to Hurt" discusses the common frustration between employees and security teams when security measures hinder productivity. It highlights a scenario where an employee needs to use AI for translating documentation but is blocked by security tools. The post emphasizes that security teams also want to enable employees to perform their tasks efficiently. It suggests that collaboration between security and other teams can help find solutions that allow access to necessary tools without compromising security. The overall message is that security doesn't have to be a barrier to productivity if there's mutual understanding and cooperation.
👉 [Read more](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS
The blog post discusses the advancements in Project Valhalla, particularly focusing on the concept of heap flattening for value classes as outlined in JEP 401. The approach to flattening value types has undergone significant changes due to a better understanding of the semantics of value types and the challenges posed by the Java language and the Java Virtual Machine (JVM). These developments aim to optimize performance and memory usage by improving how value types are handled in Java.
👉 [Read more](https://inside.java/2025/10/31/jvmls-jep-401/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector called Green Tea in Go version 1.25. This garbage collector aims to improve memory management and performance in Go applications. The post likely details the features, benefits, and potential impacts of using Green Tea, as well as how it compares to previous garbage collection methods in Go.
👉 [Read more](https://go.dev/blog/greenteagc)

