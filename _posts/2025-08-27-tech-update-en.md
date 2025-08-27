# 🛠️ 2025-08-27 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post discusses the NodeSwap feature in Kubernetes, introduced in Kubernetes v1.34, which enables swap usage on Linux nodes. This feature marks a significant departure from the traditional practice of disabling swap to ensure performance predictability. Swap allows Linux nodes to use secondary storage as additional virtual memory when physical RAM is full, potentially improving resource utilization and reducing out-of-memory (OOM) kills. However, correctly configuring Linux kernel parameters is crucial to avoid performance degradation and interference with Kubernetes' eviction logic. The article explores critical kernel parameters like `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`, explaining their roles in swap behavior and performance. The author conducted tests to evaluate the impact of these parameters, finding that proper tuning can prevent OOM kills and enhance system stability. Key recommendations include setting `vm.swappiness` to 60, `vm.min_free_kbytes` to 500MB, and `vm.watermark_scale_factor` to 2000, though these should be adjusted based on specific workload needs. Risks such as performance degradation, masking memory leaks, and disabling evictions are also highlighted, emphasizing the need for careful tuning.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - This Week in Spring - August 26th, 2025
The blog post, "This Week in Spring - August 26th, 2025," offers a quick overview of the latest updates and happenings in the Spring ecosystem, written live from SpringOne in Las Vegas. Key points include a recent episode of "A Bootiful Podcast" featuring Andrey Belyaev, the availability of Spring Boot 4.0.0.M2, Spring Batch 6.0.0.M2, and various versions of the Spring Authorization Server. It also highlights releases of Spring Modulith and a write-up by Loiane Groner on upcoming features in Spring Boot 4 and Spring Framework 7. Other notable mentions include a Docker tutorial for simplifying Spring AI builds, a Flyway tutorial with Spring Boot, discussions on CQRS with Spring Modulith, and insights from Rod Johnson on his AI framework, Embabel. The post also references a recent AWS workshop on building Java AI agents with Spring AI, a talk on Java Nullness Annotations and Kotlin by David Baker, and more. The author encourages those attending SpringOne to stop by and say hello.
👉 [Read more](https://spring.io/blog/2025/08/26/this-week-in-spring-august-26th-2025)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
The blog post titled "Prototyping an AI Tutor with Docker Model Runner" explores the potential of enhancing the developer experience using AI. It reflects on the memorable first interaction developers have with Docker's "hello-world" command and imagines how AI could improve this experience. The author, a technical writer for Docker’s Docs team, discusses their focus on developer experience and suggests that AI could play a role in making it more engaging and educational. The post likely delves into how Docker's Model Runner can be used to build an AI tutor, enhancing learning and interaction for developers.
👉 [Read more](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - How to Upgrade to Java 25 #RoadTo25
The blog post titled "How to Upgrade to Java 25 #RoadTo25" discusses the process of updating from Java 21 to Java 25. The author notes that the upgrade is generally smooth, but there are specific areas that might pose challenges, such as annotation processing, null checks, file operations, and the removal of outdated technologies. The post, authored by Peter, compiles all these potential issues to help developers navigate the transition more easily.
👉 [Read more](https://inside.java/2025/08/24/roadto25-upgrade/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post discusses the changes in the Go programming language, specifically in version 1.25, where the default setting for GOMAXPROCS has been improved to better support container environments. This update makes Go applications more efficient when running in containers by automatically adjusting the number of CPU threads to match the container's CPU limits. This enhancement aims to optimize performance and resource utilization in containerized applications.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. Helm 4 is currently in development and is expected to be released later in the year. The post encourages attendees to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion to learn more and participate in discussions. More details about Helm-related activities during the event are provided on the blog.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

