# 🛠️ 2025-11-03 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post discusses seven common pitfalls encountered when using Kubernetes and offers tips on how to avoid them. The author shares personal experiences with each issue and provides strategies to overcome them. The pitfalls include:

1. **Skipping resource requests and limits**: Failing to set CPU and memory limits can lead to resource contention or hoarding, affecting performance and stability.

2. **Underestimating liveness and readiness probes**: Not defining health checks can result in Kubernetes assuming a container is healthy when it's not responding or initializing.

3. **Relying solely on container logs**: Depending only on `kubectl logs` can lead to data loss since logs are stored locally and can be lost when containers or nodes are deleted or restarted.

4. **Treating dev and prod the same**: Using identical settings for different environments can cause issues due to varying factors like traffic patterns and resource needs.

5. **Leaving old resources active**: Not removing outdated resources can consume unnecessary cluster resources and increase costs.

6. **Diving too deep into networking**: Implementing advanced networking solutions without understanding Kubernetes basics can complicate troubleshooting.

7. **Going too light on security and RBAC**: Using insecure configurations and overly broad permissions can expose clusters to security risks.

The author emphasizes the importance of understanding Kubernetes' fundamental concepts and tailoring configurations to specific needs to prevent these common issues. The post concludes by encouraging further learning through official documentation and community resources.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
The blog post announces the release of the second release candidate (RC2) for Spring Data 2025.1.0. This release incorporates updates from Spring Framework RC3 and Spring HATEOAS RC2, focusing mainly on refinements and structural cleanups in Spring Data Commons. The team plans to release the general availability version (GA) of Spring Data 2025.1 in mid-November, coinciding with the release of Spring Framework 7.0. The post lists various modules like Spring Data JPA, MongoDB, Neo4j, and others, providing links to their respective Javadocs, documentation, and changelogs. More details can be found in the Spring Data 2025.1 Release Notes.
👉 [Read more](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
The blog post titled "Security Doesn’t Have to Hurt" discusses the common frustration of security measures interfering with employees' access to necessary tools, such as AI services for translating documentation. It highlights the shared desire of both employees and security teams to find a balance that allows work to be done efficiently without compromising security. The post likely explores how collaboration between teams can address these challenges and improve workflows without sacrificing security.
👉 [Read more](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Supercharge your JVM Performance with Project Leyden and Spring Boot
The blog post discusses the challenges faced by modern Java applications, particularly regarding startup time and time-to-peak performance, which are crucial for microservices and Kubernetes workloads. It introduces Project Leyden, an OpenJDK initiative designed to address these performance issues. The session, led by Ana and Moritz, explores how Java 25 and Spring Boot can leverage Leyden's optimizations to enhance application performance. The post provides practical techniques for immediate implementation and offers insights into the ongoing developments within Project Leyden and their implications for Java application performance.
👉 [Read more](https://inside.java/2025/11/02/devoxxbelgium-leyden-supercharge-jvm-performance/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post introduces a new experimental feature in Go 1.25 called the Green Tea Garbage Collector. This garbage collector aims to improve memory management efficiency in Go programs. It is expected to enhance performance and reduce latency, making Go applications run more smoothly. The post likely provides details on its implementation, benefits, and potential impact on Go development. Readers are encouraged to try out this new feature and share feedback to help refine it further.
👉 [Read more](https://go.dev/blog/greenteagc)

