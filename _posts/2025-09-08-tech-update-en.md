# 🛠️ 2025-09-08 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA
The tech blog post announces that the "Pod Replacement Policy" feature in Kubernetes v1.34 has reached general availability (GA). This feature provides users with control over when terminating Pods are replaced, addressing issues that arise when Pods are prematurely recreated, such as exceeding specified parallelism, scheduling delays, and unnecessary cluster scaling. Users can now choose between two policies: "TerminatingOrFailed" (default), which replaces Pods as soon as they start terminating, and "Failed," which waits until Pods fully terminate. The blog includes an example of how to configure a Job using this feature and explains the implications for popular workloads, like TensorFlow, that require specific Pod configurations. It also provides links to further documentation and acknowledgments to contributors who helped develop the feature. Readers are encouraged to get involved with the Kubernetes community for ongoing development.
👉 [Read more](https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
The blog post is about a podcast episode featuring Ryan Baxter, a notable contributor to Spring Cloud. The podcast was recorded live at the SpringOne 2025 event.
👉 [Read more](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc. has announced the acquisition of MCP Defender, a company focused on securing AI applications. This move comes as AI technology rapidly evolves from basic generative models to advanced agentic tools, significantly impacting software development. The acquisition aims to address the security challenges that come with these new AI capabilities, helping Docker enhance its cloud-native and AI-native development tools, infrastructure, and services.
👉 [Read more](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - How to Handle Security Changes in Java 25 #RoadTo25
The blog post discusses the evolving security landscape in Java 25, highlighting the deprecation of outdated algorithms and the integration of advanced cryptographic standards. Ana, in the accompanying video, reviews the key security changes introduced after JDK 21. She provides guidance on adjusting runtime security settings and preparing applications for post-quantum cryptography, which is designed to withstand attacks from quantum computers.
👉 [Read more](https://inside.java/2025/09/07/roadto25-security/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" delves into the challenges of testing asynchronous code, which is prevalent in modern software development. It highlights the complexities involved when trying to ensure the correctness and reliability of code that doesn't execute sequentially. The post explores the `testing/synctest` package, which offers tools and methodologies to effectively test asynchronous operations. This content is based on insights shared during the GopherCon Europe 2025 talk, providing practical techniques and strategies for developers to handle asynchronicities in their code testing processes.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
The blog post informs readers that the Debian/Ubuntu Helm Apt repository is transitioning from being hosted at Balto to Buildkite. Users who install Helm via Apt need to update their APT key and repository references according to the new installation instructions provided. A link to these instructions is included in the post.
👉 [Read more](https://helm.sh/blog/debian-helm-repository-move/)

