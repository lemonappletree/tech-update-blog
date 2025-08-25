# 🛠️ 2025-08-25 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post "Tuning Linux Swap for Kubernetes: A Deep Dive" explores the new NodeSwap feature in Kubernetes, expected to become stable in the v1.34 release. This feature allows the use of swap, which marks a shift from traditionally disabling swap to maintain performance predictability. The article focuses on tuning swap on Linux nodes to improve resource utilization and reduce out-of-memory (OOM) kills. It highlights that enabling swap is not straightforward and requires careful configuration of Linux kernel parameters to maintain performance and stability.

The post discusses key concepts such as anonymous vs. file-backed memory and essential kernel parameters like `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`. These parameters influence how memory is managed under pressure, affecting swap behavior, Kubernetes workloads, and eviction mechanisms. The author tested different configurations and shared findings on achieving optimal settings for stable Kubernetes clusters.

The article examines the impact of `swappiness` on memory management, the importance of tuning watermarks to prevent evictions and OOM kills, and the risks associated with enabling swap, such as performance degradation and masking memory leaks. Recommendations include starting with specific kernel parameter settings and running benchmark tests tailored to individual workloads.

Overall, the post provides detailed guidance on effectively utilizing swap in Kubernetes environments, emphasizing the need for careful tuning and testing.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
The blog post announces the release of Spring Modulith versions 2.0 M2, 1.4.3, and 1.3.9. The updates include regular dependency upgrades and minor improvements. Notably, version 2.0 M2 introduces new features such as updated event publication repository implementations for MongoDB and Neo4j, improved bootstrap procedures for `ApplicationModulesEndpoint`, and an upgrade to Spring Boot 4.0 M2. For more detailed information, readers are directed to the full changelogs linked in the post.
👉 [Read more](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post discusses the potential of enhancing the developer experience by integrating AI with Docker, specifically through the use of Docker Model Runner. The author, a technical writer on Docker's Docs team, reflects on the excitement of using Docker for the first time and explores how AI can further improve this experience. The post likely covers steps to prototype an AI Tutor using Docker Model Runner, aiming to provide developers with a more intuitive and supportive environment as they navigate Docker and its capabilities.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
The blog post titled "How to Upgrade to Java 25 #RoadTo25" discusses the process of upgrading from Java 21 to Java 25. It highlights that the transition is generally smooth, unless you're dealing with a project that has accumulated all the minor changes introduced in the new version. These changes can include updates in annotation processing, null checks, file operations, and the removal of obsolete technologies. The author, Peter, compiles these details to help developers navigate the upgrade.
👉 [Read more](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post discusses the introduction of new defaults for the GOMAXPROCS setting in Go 1.25, which are designed to enhance performance and behavior when running Go applications in containers. These updates make Go more efficient by automatically adjusting the GOMAXPROCS value to match the CPU limits set by the container, ensuring that applications utilize available resources optimally. This improvement aims to provide better resource management and performance consistency for Go applications running in containerized environments.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They will be discussing Helm 4, which is set to be released later in the year. Attendees are encouraged to join conversations with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post includes further details on Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

