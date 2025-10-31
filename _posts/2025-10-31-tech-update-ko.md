# 🛠️ 2025-10-31 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes에서 흔히 저지르는 7가지 실수와 이를 피하는 방법에 대해 설명합니다. Kubernetes는 강력하지만 때때로 좌절을 초래할 수 있으며 필자가 초기에 여러 실수를 통해 배운 점들을 공유합니다. 

1. **리소스 요청과 제한을 생략**: CPU 및 메모리 요구사항을 Pod에 명시하지 않으면 성능 저하나 실패로 이어질 수 있습니다. 적절한 요청과 제한을 설정하여 리소스 부족과 과도한 소비를 방지해야 합니다.

2. **활성 및 준비 프로브 과소평가**: 컨테이너의 상태를 확인하는 프로브를 설정하지 않으면, Kubernetes는 컨테이너가 정상적으로 작동한다고 잘못 판단할 수 있습니다.

3. **컨테이너 로그에 전적으로 의존**: `kubectl logs` 명령어만 사용하면 로그 손실 가능성이 있습니다. 로그를 중앙 집중화하여 관리해야 합니다.

4. **개발 및 프로덕션 환경을 동일하게 처리**: 환경별로 다른 요구사항을 고려하지 않으면, 특정 환경에서는 불안정하거나 성능 저하가 발생할 수 있습니다.

5. **오래된 리소스를 방치**: 사용하지 않거나 오래된 리소스를 클러스터에 남기면 리소스를 낭비하고 혼란을 초래할 수 있습니다.

6. **네트워킹에 너무 깊이 들어감**: 고급 네트워킹 솔루션을 도입하기 전에 Kubernetes의 기본 네트워킹을 충분히 이해해야 합니다.

7. **보안 및 RBAC 소홀**: 보안 구성을 신중하게 설정하지 않으면 보안 취약점이 발생할 수 있습니다.

Kubernetes는 강력하지만 자동으로 적절한 설정을 제공하지 않기 때문에 사용자가 적절한 설정을 해야 합니다. 공식 문서와 커뮤니티를 통해 더 깊이 있는 학습을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - A Bootiful Podcast: Elastic's developer advocate extraordinairre Philip Krenn on the state of logging
제목: A Bootiful Podcast: Elastic의 개발자 옹호자 필립 크렌이 전하는 로깅의 현황

요약: 안녕하세요, 스프링 팬 여러분! 이번 에피소드에서는 제 친구이자 Elastic의 뛰어난 개발자 옹호자인 필립 크렌과 함께 로깅의 현황에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/30/a-bootiful-podcast-philip-krenn)

## 🔹 Docker - theCUBE Research economic validation of Docker’s development platform
이 블로그 글은 theCUBE Research가 Docker의 개발 플랫폼이 개발자 생산성, 소프트웨어 공급망 보안, 에이전틱 AI 개발, 비용 절감 및 ROI에 미치는 영향을 조사한 독립 연구에 대한 요약입니다. 연구에서는 중대형 글로벌 기업의 IT 및 애플리케이션 개발 리더 약 400명을 대상으로 설문을 진행했습니다. 이를 통해 Docker가 개발자 생산성과 보안, 비용 효율성 등에 미치는 긍정적인 영향을 분석했습니다.
👉 [자세히 보기](https://www.docker.com/blog/thecube-research-economic-validation-of-docker-development-platform/)

## 🔹 Java - Quality Outreach Heads-up - JDK 26: HTTP/3 Support Available in HTTP Client API
블로그 글 요약: "JDK 26의 HTTP Client API에서 HTTP/3 지원이 추가되었습니다. 이 공지는 관련 프로젝트에 정기적으로 전달되는 소통의 일환입니다."
👉 [자세히 보기](https://inside.java/2025/10/30/quality-heads-up/)

## 🔹 Golang - The Green Tea Garbage Collector
블로그 글 "The Green Tea Garbage Collector"는 Go 1.25 버전에 도입된 새로운 실험적 가비지 컬렉터인 Green Tea에 대해 설명합니다. 이 가비지 컬렉터는 메모리 관리 성능을 개선하기 위한 것으로, Go 언어의 효율성을 높이는 데 초점을 맞추고 있습니다. 해당 글에서는 Green Tea의 주요 기능과 이점에 대해 다루고 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

