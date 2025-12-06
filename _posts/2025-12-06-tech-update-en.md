# 🛠️ 2025-12-06 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
The blog post provides a preview of the upcoming Kubernetes v1.35 release, highlighting key deprecations and enhancements. It notes the removal of cgroup v1 support, requiring administrators to transition to cgroup v2, and the deprecation of the ipvs mode in kube-proxy, recommending nftables instead. Support for containerd v1.y is also being phased out. Key enhancements include the introduction of a framework for nodes to declare supported features, enabling more accurate scheduling and reducing version skew issues. Kubernetes will graduate in-place updates for Pod resources to General Availability, allowing resource adjustments without restarting Pods. Pod certificates will simplify secure communication between Pods, and numeric values for taints will enable more precise scheduling based on numeric thresholds. User namespaces will enhance security by mapping container root users to unprivileged users on the host, and support for mounting OCI images as volumes will simplify data distribution and decouple data from container images. The release is scheduled for December 17, 2025, with further updates to be provided in the release notes. The blog also encourages community involvement through various channels.
👉 [Read more](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Spring AI 1.1.1 Available Now
The tech blog post announces the release of Spring AI 1.1.1, which includes 13 new features, 16 bug fixes, and essential dependency updates with security patches. Key highlights of this release are the integration with OpenAI Java SDK for improved API coverage, enhancements in Claude integration with new model support, and improvements in Google Gemini including safety ratings and thought signatures. The release also introduces stability fixes for MCP, security updates, and other enhancements such as Azure Cosmos DB Chat Memory support. The blog expresses gratitude to the community contributors and mentions the upcoming release of Spring AI 2.0.0-M1.
👉 [Read more](https://spring.io/blog/2025/12/05/spring-ai-1-1-1-available-now)

## 🔹 Docker - Docker, JetBrains, and Zed: Building a Common Language for Agents and IDEs
The blog post discusses the collaboration between Docker, JetBrains, and Zed in developing the Agent Client Protocol (ACP). As agents increasingly gain the ability to write and refactor code, the goal is for them to integrate seamlessly into the environments where developers work, such as editors. The ACP provides a shared language for agents and editors, enabling any agent to understand context, perform actions, and respond intelligently without needing custom integration. This initiative aims to enhance the interaction between agents and integrated development environments (IDEs), facilitating a more efficient development process.
👉 [Read more](https://www.docker.com/blog/docker-jetbrains-and-zed-building-a-common-language-for-agents-and-ides/)

## 🔹 Java - The Inside Java Newsletter: Register for JavaOne 2026!
The blog post is about the Inside Java Newsletter for November 2025, which highlights the registration for the upcoming JavaOne 2026 conference. The event's sessions will be announced soon, and preparations are already in progress for the conference scheduled for March 2026. The newsletter also mentions an expansion in coverage of Java User Groups while continuing to deliver the latest technical content from the Java Developer Relations team and the Java Platform Group. Readers are encouraged to visit learn.java, dev.java, and inside.java for multimedia content suitable for developers, learners, educators, and customers. Additionally, the post invites readers to explore newsletter archives, subscribe to updates, and share the newsletter with friends.
👉 [Read more](https://inside.java/2025/12/05/inside-java-newsletter/)

## 🔹 Golang - Go’s Sweet 16
The blog post celebrates the 16th anniversary of the Go programming language. It reflects on Go's journey since its inception, highlighting its growth and impact on the software development community. The post likely discusses key milestones, the language's evolution, and its contributions to modern programming practices. Additionally, it may express gratitude to the community and developers who have supported and contributed to Go's success over the years.
👉 [Read more](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
The blog post announces the release of Helm 4, which was unveiled on November 12th at the KubeCon + CloudNativeCon event. This release marks the first major version update in six years, introducing significant changes and improvements to the popular package manager for Kubernetes.
👉 [Read more](https://helm.sh/blog/helm-4-released)

