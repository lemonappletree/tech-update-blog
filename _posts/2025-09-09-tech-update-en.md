# 🛠️ 2025-09-09 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA
The blog post announces that the VolumeAttributesClass API has reached General Availability (GA) in Kubernetes v1.34. This API allows users to dynamically modify volume attributes, providing a stable way to optimize persistent storage within Kubernetes. VolumeAttributesClass acts as a "profile" for storage, enabling different quality-of-service levels or performance tiers. Users can specify a desired class of attributes in their PersistentVolumeClaim, and the Container Storage Interface (CSI) applies these changes to the volume. Key benefits include dynamically scaling performance, optimizing costs, and simplifying operations. The GA release introduces cancel support for infeasible volume modifications and quota support based on scope. Supported drivers include Amazon EBS and Google Compute Engine Persistent Disk, which allow dynamic modification of volume attributes. For further details, users can contact the SIG Storage community.
👉 [Read more](https://kubernetes.io/blog/2025/09/08/kubernetes-v1-34-volume-attributes-class/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
In this tech blog post titled "A Bootiful Podcast: Spring Cloud guru Ryan Baxter," the author discusses a podcast episode featuring Ryan Baxter, a prominent contributor to Spring Cloud. The conversation with Baxter was recorded live at the SpringOne 2025 conference.
👉 [Read more](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc. has announced the acquisition of MCP Defender, a company dedicated to securing AI applications. This move addresses the challenges associated with the rapid evolution of AI, which has significantly transformed software development. As AI tools become more advanced and agentic, they introduce new capabilities and also new security concerns. Docker aims to tackle these challenges by integrating MCP Defender's expertise in AI security, enhancing the safety of developing and deploying AI applications.
👉 [Read more](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - JDK 25 G1/Parallel/Serial GC changes
The blog post provides an overview of the changes made to the stop-the-world garbage collectors in OpenJDK with the release of JDK 25 Release Candidate 1. It focuses on updates to the G1, Parallel, and Serial garbage collectors. The post likely details improvements, optimizations, or new features introduced in this version, aimed at enhancing performance and efficiency. The specific changes would be elaborated in the full text, providing developers with insights into what to expect from these updates in JDK 25.
👉 [Read more](https://inside.java/2025/09/08/jdk25-gc-changes/)

## 🔹 Golang - Testing Time (and other asynchronicities)
The blog post titled "Testing Time (and other asynchronicities)" delves into the challenges and techniques involved in testing asynchronous code. It introduces and explores the `testing/synctest` package, which is designed to aid in the testing of asynchronous operations. The content is based on a talk from GopherCon Europe 2025, sharing insights and strategies for effectively managing and testing asynchronous processes in software development. The blog emphasizes the importance of robust testing methods to ensure the reliability and efficiency of asynchronous code.
👉 [Read more](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
The blog post announces that the Debian/Ubuntu Helm Apt repository is transitioning from being hosted at Balto to being hosted at Buildkite. Users who install Helm using Apt need to update their APT key and repository references according to the new installation instructions provided.
👉 [Read more](https://helm.sh/blog/debian-helm-repository-move/)

