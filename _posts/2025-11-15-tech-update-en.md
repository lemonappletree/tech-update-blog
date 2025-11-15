# 🛠️ 2025-11-15 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The tech blog post announces the planned retirement of Ingress NGINX by Kubernetes SIG Network and the Security Response Committee to ensure ecosystem security. Maintenance will continue until March 2026, after which there will be no updates or bug fixes. Although existing deployments will still function, users are encouraged to migrate to alternatives like the Gateway API, the modern replacement for Ingress. The post details the history and challenges faced by Ingress NGINX, citing maintenance difficulties and outdated flexibility as reasons for its retirement. The project struggled with limited maintainership, and despite efforts to find support or develop a replacement like InGate, no sustainable solutions emerged. Users are advised to begin transitioning to alternative Ingress controllers or the Gateway API immediately, as detailed in Kubernetes documentation. The blog also expresses gratitude to the maintainers of Ingress NGINX for their contributions.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Data 2025.1.0 goes GA
The blog post announces the general availability of Spring Data 2025.1.0, which is now accessible from Maven Central. This release, part of the 4.0 generation, introduces several significant updates:

1. **Upgrade to Spring Framework 7**: The latest version of the Spring Framework is now supported.
2. **Upgrade to Jakarta EE 11**: Includes updates to JPA 3.2 and Servlet 6.1.
3. **Ahead-of-Time (AOT) Repositories**: These improve startup times and reduce memory consumption by utilizing AOT compilation. They are generated during the AOT build phase and used when the application is started in AOT mode.
4. **Comprehensive Null Safety with JSpecify**: JSpecify annotations are used to express nullability, enhancing static analysis and code quality.
5. **Support for Jackson 3**: Spring Data now fully supports Jackson 3, while maintaining compatibility with Jackson 2, except for Spring Data REST, which requires Jackson 3 due to its heavy reliance on Jackson.
6. **Vector Search Methods**: These enable vector search capabilities in JPA, Apache Cassandra, MongoDB, and Neo4j, facilitating the use of existing data models in AI contexts.

The post encourages readers to check the release notes for more in-depth information on the new features.
👉 [Read more](https://spring.io/blog/2025/11/14/spring-data-2025-1-goes-ga)

## 🔹 Docker - Making the Most of Your Docker Hardened Images Trial – Part 1
The blog post titled "Making the Most of Your Docker Hardened Images Trial – Part 1" introduces the initial steps for using Docker Hardened Images to run secure, production-ready containers. It emphasizes that container base images are crucial for application security, as any vulnerabilities in these images can affect all services built on them. Docker Hardened Images tackle this issue by providing continuously-maintained, minimal base images that are designed with security in mind. These images are stripped of unnecessary packages and proactively patched to ensure a secure foundation for applications.
👉 [Read more](https://www.docker.com/blog/making-the-most-of-your-docker-hardened-images-trial-part-1/)

## 🔹 Java - Deep Dive into Gatherers - JEP Cafe #24
The tech blog post titled "Deep Dive into Gatherers - JEP Cafe #24" provides a comprehensive overview of the Gatherers feature introduced in JDK 24 and available in JDK 25. It explains how Gatherers can be used in business applications through various examples. The blog covers the basics of mapping and filtering, managing an internal mutable state, stream limiting, and sorting. It also discusses interrupting streams, avoiding resource leaks and race conditions, and optimizing performance by declaring integrators as greedy. The post highlights the ability to use Gatherers in parallel, and the use of non-parallel Gatherers in parallel streams. By the end of the video, viewers will understand how to efficiently and correctly use Gatherers, as well as when to employ them or avoid them.
👉 [Read more](https://inside.java/2025/11/14/jepcafe24/)

## 🔹 Golang - Go’s Sweet 16
The blog post celebrates the 16th birthday of the Go programming language. It reflects on Go's journey since its inception, highlighting its growth and widespread adoption over the years. The post likely discusses key milestones and achievements, the community's contributions, and the language's impact on software development. It might also touch upon future goals and developments for Go as it continues to evolve.
👉 [Read more](https://go.dev/blog/16years)

