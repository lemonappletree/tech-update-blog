# 🛠️ 2025-08-22 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post discusses the new NodeSwap feature in Kubernetes, which is set to become stable in the Kubernetes v1.34 release. This feature allows the use of swap space on Linux nodes, marking a shift from the traditional practice of disabling swap for predictability. The post delves into how to effectively tune swap on Linux nodes, emphasizing the importance of Linux kernel parameters in ensuring performance and stability under memory pressure. Key parameters like `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor` are explored for their impact on swap behavior and Kubernetes workloads.

The article describes the differences between anonymous and file-backed memory and how swap allows the system to handle memory pressure better by offloading less frequently accessed memory to disk. Through a series of stress tests on Google Cloud's GKE with Kubernetes version 1.33.2, the author demonstrates the effects of various kernel settings on swap usage, system performance, and the interaction with Kubelet's eviction logic.

The findings highlight the trade-offs between different `swappiness` settings and the importance of tuning watermarks to prevent premature evictions and OOM kills. The author suggests adjusting parameters like `min_free_kbytes` and `watermark_scale_factor` to create a larger operational zone for the kernel to manage memory pressure effectively.

The blog concludes with recommendations and risks associated with enabling swap, emphasizing the need for careful tuning to avoid performance degradation, masking memory leaks, and disabling evictions. A suggested starting point for tuning these parameters is provided, encouraging users to benchmark with their specific workloads.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - A Bootiful Podcast: Andrey Belyaev, product manager for IntelliJ IDEA
In this blog post, the author discusses a podcast episode featuring Andrey Belyaev, a Product Manager at JetBrains. The conversation focuses on the latest enhancements and support for the Spring framework within the IntelliJ IDEA product by JetBrains.
👉 [Read more](https://spring.io/blog/2025/08/21/a-bootiful-podcast-andrey-belyaev)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post discusses the potential of enhancing the developer experience using AI, specifically through the creation of an AI Tutor using Docker's Model Runner. The author, a technical writer on Docker’s Docs team, reminisces about the excitement of running a simple Docker command for the first time and imagines how AI could further improve that experience. The post likely delves into the process of prototyping an AI Tutor, exploring how AI can be integrated into Docker workflows to provide a more interactive and educational experience for developers.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
The blog post discusses Brian Goetz's session at the 2025 JVM Language Summit, where he talks about the evolution of the Java language. As the Java Language Architect, Goetz highlights the ongoing efforts to grow and enhance Java, focusing on the introduction of new features and improvements to maintain its relevance and efficiency. The session likely covers technical details about upcoming changes, challenges faced in the language's development, and the future direction of Java.
👉 [Read more](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
The tech blog post discusses the updated default behavior of GOMAXPROCS in Go 1.25, which is now optimized for running within container environments. This change improves performance by automatically adjusting the maximum number of operating system threads that can execute user-level Go code simultaneously, based on the CPU quota provided by the container. This enhancement helps ensure that Go applications efficiently utilize the available resources when running in containerized settings.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post discusses the Helm team's participation in KubeCon + CloudNativeCon EU 2025, which will take place in London, UK, from April 1 to 4. The team is preparing for the release of Helm 4 later in the year and invites attendees to engage with their maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post promises more details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

