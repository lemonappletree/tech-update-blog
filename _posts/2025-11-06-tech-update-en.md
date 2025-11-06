# 🛠️ 2025-11-06 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post titled "7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)" highlights common challenges encountered when using Kubernetes and offers strategies to avoid them. The author shares personal experiences and lessons learned through mistakes made while working with Kubernetes. The seven pitfalls discussed include:

1. **Skipping Resource Requests and Limits**: Not defining CPU and memory requirements can lead to resource starvation or hoarding. Solutions include setting modest requests, monitoring usage, and refining values.

2. **Underestimating Liveness and Readiness Probes**: Failing to define health checks can cause unresponsive applications. The author suggests adding simple probes to manage container health effectively.

3. **Relying on Container Logs**: Sole reliance on `kubectl logs` can lead to lost logs. The author recommends centralizing logs using tools like Fluentd or Fluent Bit and integrating with OpenTelemetry.

4. **Treating Dev and Prod the Same**: Using identical settings across environments can lead to issues. Customizing configurations for different environments and planning for scale in production is advised.

5. **Leaving Old Resources**: Unused resources can accumulate and increase costs. Regular audits and using tools like Kyverno to manage lifecycle policies are recommended.

6. **Diving into Advanced Networking Too Soon**: Starting with basic networking understanding is crucial before adopting complex solutions like service meshes.

7. **Neglecting Security and RBAC**: Insecure configurations can lead to vulnerabilities. Using RBAC, pinning images to specific versions, and enforcing security policies are essential practices.

The post concludes by emphasizing the importance of understanding Kubernetes deeply to avoid common pitfalls, and encourages further learning through official documentation and community engagement.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring gRPC Next Steps for 1.0.0
The blog post discusses the upcoming release of Spring gRPC 1.0.0 and its integration with Spring Boot 4. Initially, the plan was to move the autoconfiguration from Spring gRPC directly into Spring Boot for version 4.0, but due to time constraints, this has not been achieved. Instead, support for Spring Boot 4 has been added to the existing Spring gRPC project, and the 1.0 release is imminent. This setup will remain until a future milestone of Spring Boot 4.1 when the merge is expected to occur.

During the transition period from Spring gRPC 1.0 to Spring Boot 4.0, the dependencies will retain their current coordinates with a groupId of `org.springframework.grpc`. Users of Spring gRPC 0.12.0 can upgrade by simply changing the version number in their dependency management. However, some package name changes in autoconfiguration classes may require users to update imports if they are directly referenced.

Once the autoconfiguration is merged in Spring Boot 4.1, a separate BOM won't be necessary, and users will need to adjust their dependency coordinates accordingly. The blog also mentions that the autoconfiguration and starter dependencies in Spring gRPC will be deprecated immediately upon release to signal that they will be replaced in the next minor release. The transition aims to be smooth without requiring class or method deprecations.

Overall, Spring gRPC 1.0 will provide ongoing support and minimal disruption for projects already using version 0.x, with the new release depending on Spring Boot 4.0. The post promises further updates when 1.0.0-RC1 is available.
👉 [Read more](https://spring.io/blog/2025/11/11/spring-grpc-next-steps)

## 🔹 Docker - How to Use Multimodal AI Models With Docker Model Runner
The blog post discusses the integration of multimodal AI models with the Docker Model Runner. It highlights the significance of multimodal AI, which allows models to process and generate diverse input types, such as text, images, and audio. This capability enhances the interaction with AI, enabling users to input various forms of media beyond just text prompts. The post likely provides a guide or insights on implementing these advanced models using Docker's platform, emphasizing the flexibility and expanded functionality offered by multimodal AI.
👉 [Read more](https://www.docker.com/blog/how-to-use-multimodel-ai-with-model-runner/)

## 🔹 Java - JEP targeted to JDK 26: 522: G1 GC: Improve Throughput by Reducing Synchronization
The blog post discusses a targeted JEP (JDK Enhancement Proposal) for JDK 26, specifically JEP 522, which aims to improve the throughput of the G1 Garbage Collector (G1 GC) by reducing synchronization. The proposal outlines enhancements to the G1 GC that focus on minimizing synchronization overhead, potentially leading to better performance and efficiency for applications using this garbage collector. The article likely delves into the technical details of how these changes are expected to enhance throughput, contributing to the overall improvement of Java's performance in future releases.
👉 [Read more](https://inside.java/2025/11/05/jep522-target-jdk26/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector called Green Tea in Go 1.25. This new garbage collector aims to improve performance and efficiency in memory management. It is designed to optimize garbage collection processes, potentially leading to better application performance and lower latency. The post likely details the features, benefits, and potential impacts of using the Green Tea garbage collector in Go applications.
👉 [Read more](https://go.dev/blog/greenteagc)

