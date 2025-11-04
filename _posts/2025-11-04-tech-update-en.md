# 🛠️ 2025-11-04 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post discusses seven common pitfalls encountered when using Kubernetes and provides strategies to avoid them. These pitfalls include: 

1. Skipping resource requests and limits, which can lead to resource starvation or hoarding. The author recommends setting modest resource requests and limits, monitoring usage, and utilizing tools like HorizontalPodAutoscaler.
   
2. Underestimating liveness and readiness probes, which can cause unresponsive applications. Simple HTTP probes should be added to check container health and readiness.

3. Relying solely on container logs, which can lead to lost logs. The author suggests centralizing logs with tools like Fluentd or Fluent Bit and using OpenTelemetry for comprehensive monitoring.

4. Treating development and production environments the same, potentially causing instability. Customizing configurations for each environment using tools like kustomize and managing secrets with tools like Sealed Secrets is advised.

5. Leaving outdated resources in the cluster, which wastes resources and increases costs. The author recommends labeling resources, auditing the cluster regularly, and using tools like Kyverno for policy automation.

6. Diving too deep into networking too soon, which can complicate troubleshooting. A basic understanding of Kubernetes networking should be attained before implementing advanced solutions like service meshes.

7. Going too light on security and RBAC, leaving clusters vulnerable. The author advises defining roles and permissions with RBAC, pinning images to specific versions, and enforcing security policies.

The author concludes by emphasizing that Kubernetes needs explicit instructions to function correctly, and understanding these pitfalls can prevent unnecessary headaches. They encourage further learning through official Kubernetes documentation and community resources.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring AI 1.1.0-M4 Available Now
The tech blog post announces the release of Spring AI version 1.1.0-M4, which is now available on Maven Central. This patch release emphasizes stability enhancements and bug fixes. It includes 340 updates, consisting of 35 functionality improvements, 132 bug fixes, and 41 documentation enhancements. Key highlights mention significant improvements in functionality, stability, and documentation, as well as updated dependencies for better security and performance. Enhanced functional areas include Model Context Protocol (MCP) 0.15.0 updates, recursive advisor execution, Anthropic Citations API support, OpenAI File API integration, AWS Bedrock prompt caching, and Oracle JDBC chat memory support. The team is working towards releasing RC and 1.1.0-GA soon. Contributors and resources are acknowledged, encouraging community engagement and contributions.
👉 [Read more](https://spring.io/blog/2025/11/03/spring-ai-1-1-0-M4-available-now)

## 🔹 Docker - How to Use Multimodal AI Models With Docker Model Runner
The blog post discusses the integration of multimodal AI models with Docker Model Runner, highlighting the advancements in AI that allow models to process and generate multiple types of inputs, such as text, images, and audio. This capability enhances the interaction with AI, moving beyond just text prompts to include images and sounds. The post likely provides a guide on how to set up and use Docker Model Runner to leverage these multimodal models, making it easier for developers to implement and experiment with such advanced AI capabilities in their applications.
👉 [Read more](https://www.docker.com/blog/how-to-use-multimodel-ai-with-model-runner/)

## 🔹 Java - Quality Outreach Heads-up - JDK 25: Consistent Behavior of ‘new File(“”)’
The blog post titled "Quality Outreach Heads-up - JDK 25: Consistent Behavior of ‘new File(“”)’" provides an update on a change in the behavior of `File` instances created with an empty path in JDK 25. This communication is part of the regular updates sent to projects involved in the Quality Outreach program. The change aims to ensure consistent behavior when creating `File` objects with an empty string, which is crucial for developers to understand and adapt their applications accordingly. For more details, the complete post can be accessed through the provided link.
👉 [Read more](https://inside.java/2025/11/03/quality-heads-up/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post discusses the introduction of a new experimental garbage collector called Green Tea in Go 1.25. This garbage collector aims to improve memory management and performance in the Go programming language. The post likely covers the benefits and potential impact of Green Tea on Go applications, highlighting its experimental status and encouraging developers to test and provide feedback.
👉 [Read more](https://go.dev/blog/greenteagc)

