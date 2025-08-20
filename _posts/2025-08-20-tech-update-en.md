# 🛠️ 2025-08-20 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post discusses the upcoming stabilization of the NodeSwap feature in Kubernetes v1.34, which allows swap usage on Linux nodes. Traditionally, swap was disabled in Kubernetes for performance predictability. The post emphasizes the need for careful tuning of Linux kernel parameters to optimize swap performance and avoid issues like performance degradation and interference with Kubelet's eviction logic. Key parameters include `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`. The author conducted tests on a GKE setup, varying these parameters to observe their impact on memory management and node stability. Findings suggest that while enabling swap can improve resource utilization and prevent OOM kills, it requires careful configuration to avoid performance issues. The post concludes with recommendations for initial parameter settings and advises benchmarking with specific workloads to fine-tune configurations.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Authorization Server 2.0.0-M2, 1.5.2 and 1.4.5 available now
The tech blog post announces the release of Spring Authorization Server versions 2.0.0-M2, 1.5.2, and 1.4.5. It encourages users to check the release notes for each version for detailed information. To help users get started, the post provides links to the Getting Started chapter of the reference documentation and sample projects for setup and configuration. Additionally, it includes links to the project page and GitHub issues for further exploration and support.
👉 [Read more](https://spring.io/blog/2025/08/19/spring-authorization-server-2-0-0-M2-1-5-2-and-1-4-5-available-now)

## 🔹 Docker - Streamline NGINX Configuration with Docker Desktop Extension
The blog post discusses how to simplify NGINX configuration using a Docker Desktop Extension, contributed by Dylen Turnbull and Timo Stark. Dylen Turnbull, with extensive experience in enterprise and open-source software development, shares insights from his roles at companies like Symantec, Veritas, and F5 Networks, and his current position as a Developer Advocate for NGINX. The post is part of Docker's ongoing series highlighting use cases and success stories from its partners and practitioners.
👉 [Read more](https://www.docker.com/blog/streamline-nginx-configuration-with-docker-desktop-extension/)

## 🔹 Java - Auto-Vectorization in HotSpot #JVMLS
The blog post discusses a video presentation on the development and improvements of HotSpot C2's auto-vectorizer. It starts with an introduction to the SuperWord algorithm and then explores the significant enhancements that have already been made. The presenter also outlines future plans for advancements in this area, using real-world examples and benchmarks to illustrate the progress and potential of auto-vectorization in HotSpot.
👉 [Read more](https://inside.java/2025/08/16/jvmls-hotspot-auto-vectorization/)

## 🔹 Golang - Go 1.25 is released
The blog post announces the release of Go 1.25, highlighting several new features and improvements. Key updates include the introduction of container-aware GOMAXPROCS, which optimizes the setting of maximum CPU threads based on container limits. A new testing/synctest package has been added to enhance testing capabilities. Additionally, there are experimental features such as a new garbage collector (GC) and an updated version of the encoding/json package, referred to as encoding/json/v2. These updates aim to improve performance, testing, and functionality in the Go programming language.
👉 [Read more](https://go.dev/blog/go1.25)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They will be discussing the upcoming release of Helm 4, and attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth at the Project Pavilion. More details about Helm-related activities throughout the week are provided in the full post.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

