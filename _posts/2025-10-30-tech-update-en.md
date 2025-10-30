# 🛠️ 2025-10-30 Tech Update Summary

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
The blog post discusses seven common pitfalls encountered when using Kubernetes and offers advice on how to avoid them. The author shares personal experiences and lessons learned to guide both beginners and those managing production clusters. Key pitfalls include:

1. **Skipping Resource Requests and Limits**: Ignoring CPU and memory specifications can lead to resource starvation or hoarding. It's crucial to start with modest requests and monitor usage to adjust accordingly.

2. **Underestimating Liveness and Readiness Probes**: Not setting these probes can result in traffic being sent to unresponsive containers. Simple health checks can prevent premature traffic and unnecessary downtimes.

3. **Relying Solely on Container Logs**: Using only `kubectl logs` is risky as logs can be lost after container restarts. Centralizing logs using tools like Fluentd and pairing them with metrics provides a more reliable solution.

4. **Treating Dev and Prod Identically**: Using the same configurations for different environments can cause issues due to varying resource needs. Customizing settings for each environment is recommended.

5. **Leaving Old Resources**: Unused resources can accumulate and waste resources. Regular audits and labeling can help manage this effectively.

6. **Diving Into Networking Too Soon**: Implementing advanced networking solutions without understanding Kubernetes' basic networking can complicate troubleshooting. It's advised to begin with basic configurations and only scale complexity when needed.

7. **Neglecting Security and RBAC**: Using insecure defaults, like running containers as root or using broad RBAC roles, poses security risks. Implementing strict security policies and role-based access controls is imperative.

The author concludes by emphasizing that Kubernetes requires explicit instructions to function as desired and shares resources for further exploration, encouraging community engagement and learning.
👉 [Read more](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Reactive Support in Spring for Apache Pulsar Will Be Discontinued
The blog post announces that the Reactive support in the Spring for Apache Pulsar project will be discontinued. This decision is a result of evaluating adoption metrics, download trends, and project activity, leading to the retirement of this functionality to better focus on areas with higher community demand. The discontinuation means that the `spring-pulsar-reactive` module will be removed starting with version 2.0.0 of Spring for Apache Pulsar, and Spring Boot will also remove support for these components starting with version 4.0.0. Despite this change, the team remains committed to the ongoing development of the Spring for Apache Pulsar project. The post thanks contributors to the Reactive support and invites users to reach out with any questions or concerns.
👉 [Read more](https://spring.io/blog/2025/10/29/spring-pulsar-reactive-discontinued)

## 🔹 Docker - How to add MCP Servers to Claude Desktop with Docker MCP Toolkit
The blog post discusses how to enhance Claude Desktop by integrating it with real developer tools using the Docker MCP Toolkit. The aim is to transform Claude from merely a conversational assistant into a development partner capable of performing tasks safely and securely without interacting with your local machine. The article provides guidance on using the Docker MCP Toolkit to connect MCP Servers to Claude Desktop, thus enabling more robust development capabilities. This integration represents a significant advancement for users looking to leverage Claude Desktop for development purposes.
👉 [Read more](https://www.docker.com/blog/connect-mcp-servers-to-claude-desktop-with-mcp-toolkit/)

## 🔹 Java - AI World: Georges Saab Unveils Java 25 for AI and Cloud
The blog post discusses the unveiling of Java 25 by Georges Saab at Oracle AI World 2025. It highlights how Java 25 is designed to enhance AI, modernize enterprise applications, and support cloud-native development. The post encourages readers to watch an Oracle TV segment for expert insights into the latest innovations of the Java 25 platform.
👉 [Read more](https://inside.java/2025/10/29/aiworld-java-for-ai/)

## 🔹 Golang - The Green Tea Garbage Collector
The blog post introduces a new experimental garbage collector called Green Tea, which is included in Go version 1.25. This garbage collector is designed to improve memory management and performance in Go applications. The post likely discusses the features and advantages of Green Tea, how it differs from previous garbage collectors in Go, and any potential impacts on developers using this new version. Readers are encouraged to explore the linked article for more detailed information on the implementation and benefits of the Green Tea garbage collector.
👉 [Read more](https://go.dev/blog/greenteagc)

