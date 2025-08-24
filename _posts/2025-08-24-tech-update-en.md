# 🛠️ 2025-08-24 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post "Tuning Linux Swap for Kubernetes: A Deep Dive" discusses the upcoming stabilization of the NodeSwap feature in Kubernetes v1.34, which allows the use of swap space on Linux nodes. This feature enables nodes to utilize secondary storage for virtual memory when physical RAM is exhausted, aiming to enhance resource utilization and reduce out-of-memory (OOM) incidents. However, effective swap usage requires careful tuning of Linux kernel parameters like `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`. Misconfiguration can degrade performance and interfere with Kubernetes' eviction logic. The post explores the impact of these parameters through stress tests, showing how optimal configurations can prevent OOM kills and improve node stability. It highlights the trade-offs between aggressive and conservative swap usage based on workload needs and recommends starting configurations for swap-enabled Linux nodes. The article advises benchmarking these settings with actual workloads to ensure optimal performance and stability.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
The blog post announces the release of Spring Modulith versions 2.0 M2, 1.4.3, and 1.3.9. The latest versions include bug fixes, dependency upgrades, and minor improvements. Significant updates in the 2.0 M2 release include enhancements to the event publication repository implementation for MongoDB and Neo4j, improved bootstrap procedures for `ApplicationModulesEndpoint`, and an upgrade to Spring Boot 4.0 M2. More information is available in the full changelogs linked in the post.
👉 [Read more](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post discusses the concept of enhancing the developer experience by using AI to create a more interactive and educational environment. The author, a technical writer on Docker's Docs team, reflects on the initial excitement of using Docker through the simple command `docker run hello-world`. The post explores the idea of developing an AI Tutor using Docker's Model Runner to improve learning and engagement for developers. This AI Tutor could potentially guide users through complex processes, offer personalized assistance, and make the Docker learning journey more efficient and enjoyable.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
The blog post discusses a session led by Brian Goetz, the Java Language Architect, at the 2025 JVM Language Summit. The session focuses on the ongoing evolution of the Java language. It highlights the strategies and considerations involved in developing and enhancing Java to meet modern needs while maintaining its core principles. The talk likely covers new features, improvements, and the future direction of Java, emphasizing the language's growth and adaptation over time.
👉 [Read more](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post discusses the improvements in Go version 1.25 related to the GOMAXPROCS setting, which controls the maximum number of operating system threads that can execute user-level Go code simultaneously. The update introduces container-aware defaults for GOMAXPROCS, enhancing the performance of Go applications running in containerized environments. This change helps ensure that Go programs allocate CPU resources more efficiently based on the container's limits rather than the host machine's capabilities, leading to better resource management and performance in containerized applications.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They are working on Helm 4, which is expected to be released later in the year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides further details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

