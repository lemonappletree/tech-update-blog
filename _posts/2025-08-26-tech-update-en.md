# 🛠️ 2025-08-26 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post titled "Tuning Linux Swap for Kubernetes: A Deep Dive" discusses the upcoming NodeSwap feature in Kubernetes v1.34, which allows swap usage on Linux nodes, diverging from the traditional practice of disabling swap for performance predictability. This feature aims to enhance resource utilization and reduce out-of-memory (OOM) kills by using secondary storage for additional virtual memory when physical RAM is exhausted. However, enabling swap requires careful tuning of Linux kernel parameters to maintain node performance and stability under memory pressure.

The post explores key Linux kernel parameters that influence swapping behavior, such as `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`. These parameters help manage memory reclamation, swap usage, and eviction mechanisms. The author shares findings from stress tests conducted on GKE nodes, showing how different configurations impact Kubernetes workload performance and stability.

Key insights include the importance of setting appropriate `swappiness` values based on workload characteristics, and tuning watermarks to prevent premature evictions and OOM kills. The blog also highlights the risks of performance degradation, masking memory leaks, and disabling evictions if swap is not properly managed.

For Kubernetes nodes with swap enabled, the author recommends starting with a `vm.swappiness` of 60, `vm.min_free_kbytes` of 500MB, and `vm.watermark_scale_factor` of 2000, but emphasizes the need for workload-specific benchmarking to optimize settings.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
The blog post announces the release of Spring Modulith versions 2.0 M2, 1.4.3, and 1.3.9. These updates include regular dependency upgrades and minor improvements. Notable features in the 2.0 M2 release are the updated event publication repository implementations for MongoDB and Neo4j, improved bootstrap procedure for `ApplicationModulesEndpoint`, and an upgrade to Spring Boot 4.0 M2. More information can be found in the full changelogs linked in the post.
👉 [Read more](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post discusses enhancing the developer experience by using AI in conjunction with Docker, particularly through the Docker Model Runner. The author, a technical writer on Docker's Docs team, reflects on the excitement of running a simple Docker command for the first time and explores how AI can improve this experience. The post likely delves into how developers can prototype an AI tutor using Docker Model Runner, emphasizing the potential for AI to make learning and using Docker more engaging and efficient.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
The blog post titled "How to Upgrade to Java 25 #RoadTo25" discusses the process of updating from Java 21 to Java 25. It describes the transition as generally smooth but notes that some projects may face challenges due to changes in specific areas. These areas include annotation processing, null checks, file operations, and the removal of outdated technologies. The author, Peter, compiles these potential issues to provide a comprehensive guide for developers navigating these updates.
👉 [Read more](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post discusses the new default settings for GOMAXPROCS introduced in Go 1.25, which enhance its performance when running in containerized environments. These changes aim to optimize the way Go applications handle CPU resources within containers, leading to more efficient resource usage and better application behavior. The update ensures that Go applications can automatically adjust to the CPU limits specified by the container runtime, improving performance and resource management without requiring manual configuration.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London from April 1-4. It highlights that Helm 4 is currently being developed and encourages attendees to engage with the maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post provides more details about the Helm-related activities planned for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

