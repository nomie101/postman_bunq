{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "722224b3-a449-4319-957e-30fe1247b1ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import findspark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "983160f3-268b-48ec-a754-edc706816763",
   "metadata": {},
   "outputs": [],
   "source": [
    "findspark.init()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "60aab027-cae0-4e65-8de0-1eb49527ba81",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyspark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "99f1cf48-c428-436b-8041-ff917e7476bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from pyspark.sql import SparkSession"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6b65acc9-b995-4d60-819a-6df8b4ea648b",
   "metadata": {},
   "outputs": [],
   "source": [
    "spark=SparkSession.builder.appName('Practice').config(\"spark.jars.packages\",\"com.crealytics:spark-excel_2.12:0.13.7\").getOrCreate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9f495b36-1df6-46f5-b4ea-8e5910d29c91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <div>\n",
       "                <p><b>SparkSession - in-memory</b></p>\n",
       "                \n",
       "        <div>\n",
       "            <p><b>SparkContext</b></p>\n",
       "\n",
       "            <p><a href=\"http://host.docker.internal:4041\">Spark UI</a></p>\n",
       "\n",
       "            <dl>\n",
       "              <dt>Version</dt>\n",
       "                <dd><code>v3.3.0</code></dd>\n",
       "              <dt>Master</dt>\n",
       "                <dd><code>local[*]</code></dd>\n",
       "              <dt>AppName</dt>\n",
       "                <dd><code>Practice</code></dd>\n",
       "            </dl>\n",
       "        </div>\n",
       "        \n",
       "            </div>\n",
       "        "
      ],
      "text/plain": [
       "<pyspark.sql.session.SparkSession at 0x2b65b0ab580>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spark\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "159e7cd2-df62-4f50-83c4-750626b54a38",
   "metadata": {},
   "source": [
    "# READ BUNQ STATEMEENT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bc7e4171-0d7c-401a-a0f9-ffea6aad5f77",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import base64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ea88f5c3-c8ad-4ae8-b1cb-9b94844e853e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "945e532d-098b-4407-8993-8000aed97e03",
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_onedrive_directdownload (onedrive_link):\n",
    "    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))\n",
    "    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip(\"=\")\n",
    "    resultUrl = f\"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content\"\n",
    "    return resultUrl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "305a5eb8-dfd0-440f-ae0c-20f9f07a8791",
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_files(file):\n",
    "    df_file=spark.read.format(\"com.crealytics.spark.excel\") \\\n",
    "    .option(\"header\", \"true\") \\\n",
    "    .option(\"inferSchema\", \"true\") \\\n",
    "    .load(file)\n",
    "    return df_file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "125bab3b-3f43-4c01-81bf-d52dfc0e3761",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {s
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
