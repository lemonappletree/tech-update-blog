# 🛠️ 2025-08-23 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post "Tuning Linux Swap for Kubernetes: A Deep Dive" explores the recently introduced NodeSwap feature in Kubernetes, anticipated to become stable in the upcoming v1.34 release. This feature allows the use of swap space, marking a shift from the traditional practice of disabling swap for performance consistency. The article delves into optimizing swap on Linux nodes to enhance resource utilization and minimize out-of-memory (OOM) incidents by using swap as additional virtual memory when physical RAM is depleted. 

It highlights the critical role of Linux kernel parameters in managing swap behavior and their impact on Kubernetes workloads. The blog describes how to configure these parameters, such as `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`, to balance node stability and performance under memory pressure. The author shares insights from stress tests conducted in a Google Cloud environment, illustrating the effects of different swap settings on system performance and Kubernetes eviction logic.

The post concludes with recommendations for configuring swap on Linux nodes, advising a starting point of `vm.swappiness=60`, `vm.min_free_kbytes=500MB`, and `vm.watermark_scale_factor=2000`, while emphasizing the importance of benchmarking these settings against specific workload requirements to ensure optimal performance and stability in Kubernetes clusters.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
The blog post announces the release of Spring Modulith versions 2.0 M2, 1.4.3, and 1.3.9. The updates include routine dependency upgrades and minor improvements in the bugfix releases. The 2.0 M2 version introduces new features like updated event publication repository implementations for MongoDB and Neo4j, improvements in the bootstrap procedure for `ApplicationModulesEndpoint`, and an upgrade to Spring Boot 4.0 M2. More detailed information can be found in the full changelogs linked in the post.
👉 [Read more](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post discusses the potential of enhancing developer experiences with AI by using Docker Model Runner to prototype an AI tutor. The author, a technical writer for Docker's Docs team, reflects on the excitement of running a basic Docker command and considers how AI could improve such experiences. The post likely explores the process of setting up an AI tutor, utilizing Docker's capabilities to streamline and enhance learning and development in the tech community.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
The blog post covers a session led by Brian Goetz, the Java Language Architect, during the 2025 JVM Language Summit. The session focuses on the evolution and growth of the Java language. It discusses the ongoing efforts and strategies to enhance Java, addressing current challenges and future directions. The aim is to ensure Java remains modern, efficient, and relevant to developers by incorporating new features and improvements.
👉 [Read more](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post titled "Container-aware GOMAXPROCS" discusses the improvements made in Go version 1.25 regarding the GOMAXPROCS setting, which determines the maximum number of CPUs that can execute Go code simultaneously. The update introduces new default settings that enhance the performance of Go applications running in containerized environments. This change allows Go programs to more effectively utilize the available CPU resources within containers, leading to better efficiency and performance. The post likely details the technical aspects of these improvements and their impact on Go applications.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London, UK, from April 1 to 4. The team will discuss the upcoming release of Helm 4 and engage with attendees during talk sessions and at the Helm booth in the Project Pavilion. The post encourages readers to join the conversation and provides more details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

