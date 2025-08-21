# 🛠️ 2025-08-21 Tech Update Summary

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
The blog post "Tuning Linux Swap for Kubernetes: A Deep Dive" discusses the upcoming Kubernetes v1.34 release's NodeSwap feature, which allows swap usage on Linux nodes. This is a significant change from the traditional approach of disabling swap for performance predictability. The feature aims to enhance resource utilization and minimize out-of-memory (OOM) kills by using secondary storage when physical RAM is exhausted. However, enabling swap requires careful tuning of Linux kernel parameters to avoid performance degradation and interference with Kubelet’s eviction logic.

The blog provides an in-depth analysis of key Linux kernel parameters that affect swap behavior, including `vm.swappiness`, `vm.min_free_kbytes`, and `vm.watermark_scale_factor`. Through stress tests conducted on GKE with Kubernetes version 1.33.2, different scenarios were evaluated to determine the impact of these parameters on swap utilization, workload performance, and eviction mechanisms. Findings indicate that the choice of `swappiness` value should be workload-dependent, balancing between I/O latency sensitivity and file cache needs.

The post also emphasizes the importance of tuning watermarks to prevent premature evictions and OOM kills by increasing `min_free_kbytes` and `watermark_scale_factor`. This adjustment provides a larger buffer for the `kswapd` process to manage memory under pressure effectively.

In conclusion, while enabling swap can be beneficial, it carries risks such as performance degradation and masking memory leaks. Proper tuning is crucial to maintain stability and prevent disabling of Kubernetes evictions. The post recommends starting with specific kernel parameter settings and encourages benchmarking with individual workloads to identify optimal configurations.
👉 [Read more](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Batch 6.0.0-M2 available now
The tech blog post announces the release of Spring Batch 6.0.0-M2, which is now available on Maven Central. This milestone release includes several updates and improvements such as upgraded dependencies, a new implementation of the chunk-oriented processing model, and the ability to recover abruptly failed job executions. The Spring dependencies have been updated to new milestones of Spring Framework, Spring Integration, Spring AMQP, Spring Kafka, Spring Data, Spring Ldap, and Micrometer. The new chunk-oriented processing model offers an enhanced implementation that replaces the previous classes and is now stable in version 6.0. Additionally, the release introduces a method in the JobOperator interface to consistently recover failed job executions across all job repositories. Users are encouraged to check the release notes for detailed changes and refer to the migration guide for transitioning to the new implementation. Feedback is welcomed through GitHub and other platforms.
👉 [Read more](https://spring.io/blog/2025/08/20/spring-batch-6)

## 🔹 Docker - The Supply Chain Paradox: When “Hardened” Images Become a Vendor Lock-in Trap
The blog post discusses the growing market for pre-hardened container images, which offer instant security with minimal operational effort. These images are appealing because they come with built-in security features, allowing teams to concentrate on application development and deployment instead of dealing with detailed configuration management. However, the post warns that relying on these hardened images can lead to vendor lock-in, as organizations might become dependent on specific vendors for updates and support. This paradox highlights a trade-off between achieving quick security benefits and risking reduced flexibility in choosing or switching vendors.
👉 [Read more](https://www.docker.com/blog/hardened-container-images-security-vendor-lock-in/)

## 🔹 Java - Auto-Vectorization in HotSpot #JVMLS
The blog post discusses a video presentation on the development and improvements of the auto-vectorizer in HotSpot C2. It starts with an introduction to the SuperWord algorithm and then details significant enhancements that have already been implemented. The presenter also shares future advancement plans, using real-world examples and benchmarks to illustrate these points.
👉 [Read more](https://inside.java/2025/08/16/jvmls-hotspot-auto-vectorization/)

## 🔹 Golang - Container-aware GOMAXPROCS
The blog post discusses improvements in Go 1.25 related to the GOMAXPROCS setting, which controls the maximum number of CPU cores that can be executing simultaneously. In this update, the defaults for GOMAXPROCS have been optimized to better support containerized environments, where resource limits are often imposed. This change enhances the performance and efficiency of Go applications running in containers by ensuring they are more aware of and responsive to the resources available within the container.
👉 [Read more](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. Attendees can engage with Helm maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post highlights Helm 4, which is set to be released later in the year, and encourages participation in discussions about it. More details on Helm-related activities throughout the event are provided in the post.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

