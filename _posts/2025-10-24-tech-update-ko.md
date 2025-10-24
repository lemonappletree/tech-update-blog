# 🛠️ 2025-10-24 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes를 사용하면서 흔히 겪을 수 있는 7가지 실수와 이를 피하기 위한 방법에 대해 설명합니다. 글쓴이는 초기 Kubernetes 사용 시 많은 실수를 했으며, 이를 통해 배운 점을 공유하고자 합니다. 주요 내용은 다음과 같습니다:

1. **리소스 요청 및 제한 설정 누락**: CPU와 메모리 요구사항을 설정하지 않으면 리소스 부족이나 과다 사용으로 문제가 발생할 수 있습니다.
2. **라이브니스 및 레디니스 프로브 과소평가**: 컨테이너 상태를 모니터링하는 프로브를 설정하지 않으면 애플리케이션이 비정상적으로 작동할 때 감지할 수 없습니다.
3. **컨테이너 로그 의존**: `kubectl logs`만 사용하면 로그 손실 위험이 있으며, 로그를 중앙 집중화하는 것이 중요합니다.
4. **개발 및 프로덕션 환경 동일하게 처리**: 환경별로 다른 요구사항을 반영하지 않으면 성능과 보안 문제가 발생할 수 있습니다.
5. **오래된 리소스 방치**: 사용하지 않는 리소스를 남겨두면 클러스터 자원이 낭비됩니다.
6. **초기에 네트워킹에 과도하게 집중**: Kubernetes의 기본 네트워킹을 충분히 이해하지 않고 복잡한 네트워킹 솔루션을 도입하면 문제 해결이 어렵습니다.
7. **보안과 RBAC 소홀히 하기**: 보안 설정을 소홀히 하면 클러스터가 위험에 노출될 수 있습니다.

글쓴이는 이러한 실수를 피하기 위한 구체적인 방법도 제시하며, Kubernetes 사용 시 주의해야 할 점을 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring team engineer Dariusz Jędrzejczyk on the latest-and-greatest in the reactive world, MCP, and more
블로그 글은 Spring 팀 엔지니어인 Dariusz Jędrzejczyk와의 팟캐스트 대화를 기반으로 하고 있습니다. 이 대화에서는 리액티브 월드의 최신 기술, MCP 등에 대해 논의합니다. Spring 팬들에게 리액티브 프로그래밍과 관련된 최신 정보와 통찰력을 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/23/a-bootiful-podcast-dariusz-j%C4%99drzejczyk)

## 🔹 Docker - Docker + E2B: Building the Future of Trusted AI
이 기술 블로그 글은 Docker와 E2B를 활용하여 신뢰할 수 있는 AI의 미래를 구축하는 방법에 대해 다룹니다. 요약하자면, 소프트웨어의 신뢰는 여기서 시작됩니다. 에이전트 시대가 도래하면서 많은 팀들이 실험을 하고 있으며, 일부는 이제 막 시작했지만, 이미 운영 중인 팀도 있습니다. 이 과정에서 가장 큰 과제는 신뢰성입니다. 에이전트가 안전하게 작동할 것이라는 신뢰가 필요합니다. 이미 2천만 명 이상의 개발자가 Docker를 사용하여 소프트웨어를 안전하게 구축하고 배포하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-e2b-building-the-future-of-trusted-ai/)

## 🔹 Java - Three Upcoming G1 Improvements - Inside Java Newscast #99
기술 블로그 글의 제목은 "다가오는 G1 개선 사항 - Inside Java Newscast #99"입니다. Java의 거의 기본 가비지 수집기인 G1에 대한 몇 가지 개선 사항이 논의되고 있습니다. 이미 병합된 JEP 522는 처리량을 개선하기 위해 두 번째 카드 테이블을 도입하고 있으며, JEP 523 후보는 이전에 Serial GC가 사용되던 곳에서도 G1을 기본으로 설정하려고 합니다. 또한, G1과 ZGC를 위한 자동 힙 크기 조정에 대한 초안 제안도 포함되어 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/23/newscast-99/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구로서 새로운 기능인 "플라이트 레코더"가 도입되었습니다. 이 도구는 소프트웨어의 실행 상태를 기록하고 분석하여 문제를 진단하는 데 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
제목: 헬름(Helm) 10주년

요약: 10년 전, Kubernetes 1.1.0 릴리스 직후의 해커톤에서 헬름이 탄생했습니다. 헬름의 첫 커밋은 헬름 버전 1의 코드베이스가 있는 helm-classic Git 리포지토리에서 확인할 수 있습니다. 이는 헬름이 Deployment Manager와 통합되고 Kubernetes 프로젝트에 포함되기 전의 원래 헬름입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

