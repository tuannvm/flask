-- ----------------------------
--  Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS "public"."orders";
CREATE TABLE "public"."orders" (
	"customer_id" int4,
	"id" int4 NOT NULL,
	"product" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);

-- ----------------------------
--  Records of orders
-- ----------------------------
BEGIN;
INSERT INTO "public"."orders" VALUES ('1', '1', 'Chair');
INSERT INTO "public"."orders" VALUES ('1', '2', 'Pen');
INSERT INTO "public"."orders" VALUES ('1', '3', 'Monitor');
INSERT INTO "public"."orders" VALUES ('3', '4', 'Headphones');
COMMIT;

-- ----------------------------
--  Primary key structure for table orders
-- ----------------------------
ALTER TABLE "public"."orders" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;

-- ----------------------------
--  Foreign keys structure for table orders
-- ----------------------------
ALTER TABLE "public"."orders" ADD CONSTRAINT "fk_customer_order" FOREIGN KEY ("customer_id") REFERENCES "public"."customers" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;